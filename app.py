"""
app.py

Application Flask pour la conversion de bases numériques.

Fonctionnalités principales :
- Fournit une interface web pour convertir des nombres entre les bases binaire, octale, décimale et hexadécimale.
- API RESTful (/api/convert) permettant la conversion de valeurs envoyées en JSON.
- Validation des entrées selon la base sélectionnée.
- Conversion bidirectionnelle entre toutes les bases supportées.
- Affichage des résultats de conversion et gestion des erreurs côté serveur.

Auteur : Gauthier Shimatu (Le shimatologue)
Lien GitHub : https://github.com/gshimatu
Version : 1.3
Date de création : 2025-05-19
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change_me")

def to_decimal(value, base):
    """Convertit une valeur d'une base donnée vers la base décimale."""
    try:
        return int(str(value), base)
    except ValueError:
        return None

def from_decimal(value, base):
    """Convertit une valeur décimale vers une base donnée."""
    if not isinstance(value, int):
        return None
    if base == 2:
        return bin(value)[2:]
    elif base == 8:
        return oct(value)[2:]
    elif base == 10:
        return str(value)
    elif base == 16:
        return hex(value)[2:].upper()
    return None

def to_decimal_steps(value_str, base):
    """Convertit une valeur en décimal en détaillant les étapes."""
    steps = []
    value_str = value_str.lower()
    chars = list(value_str)
    chars.reverse()
    total = 0
    for i, c in enumerate(chars):
        if base == 16:
            n = int(c, 16)
        else:
            n = int(c)
        step = f"{c} × {base}^{i} = {n * (base ** i)}"
        steps.append(step)
        total += n * (base ** i)
    steps.reverse()
    steps.append(f"Total = {total}")
    return total, steps

def get_conversion_steps(value_str, from_base, to_base):
    """Retourne les étapes de conversion de value_str (from_base) vers to_base."""
    steps = []
    # 1. Conversion en décimal (toujours nécessaire)
    try:
        decimal = int(value_str, from_base)
    except Exception:
        return ["Valeur invalide."]
    if to_base == 10:
        # Étapes pour aller vers décimal
        chars = list(value_str.lower())
        chars.reverse()
        total = 0
        for i, c in enumerate(chars):
            n = int(c, from_base)
            step = f"{c} × {from_base}^{i} = {n * (from_base ** i)}"
            steps.append(step)
            total += n * (from_base ** i)
        steps.reverse()
        steps.append(f"Total = {total}")
        return steps
    else:
        # Étapes pour aller vers octal ou hexadécimal
        steps.append(f"Conversion en décimal : {value_str} (base {from_base}) = {decimal} (base 10)")
        if to_base == 8:
            result = oct(decimal)[2:]
            steps.append(f"Conversion du décimal {decimal} en octal : {result}")
        elif to_base == 16:
            result = hex(decimal)[2:].upper()
            steps.append(f"Conversion du décimal {decimal} en hexadécimal : {result}")
        return steps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/steps')
def steps():
    # Récupère les infos de la session
    value = session.get("last_input_value", "")
    from_base = session.get("last_from_base", 10)
    bases = [
        {"name": "Octal", "base": 8},
        {"name": "Décimal", "base": 10},
        {"name": "Hexadécimal", "base": 16}
    ]
    # Base cible par défaut (décimal)
    selected_base = int(request.args.get("to_base", 10))
    steps_dict = {}
    for b in bases:
        if b["base"] != from_base:
            steps_dict[b["base"]] = get_conversion_steps(value, from_base, b["base"])
    return render_template(
        "steps.html",
        bases=[b for b in bases if b["base"] != from_base],
        selected_base=selected_base,
        steps=steps_dict.get(selected_base, [])
    )

@app.route('/api/convert', methods=['POST'])
def convert_api():
    data = request.get_json()
    if not data or 'value' not in data or 'from_base' not in data:
        return jsonify({"error": "Données invalides"}), 400

    input_value_str = str(data.get('value')).strip()
    from_base = data.get('from_base')

    if not input_value_str:
        return jsonify({"error": "La valeur ne peut pas être vide"}), 400

    # Validation de la base
    try:
        from_base = int(from_base)
        if from_base not in [2, 8, 10, 16]:
            return jsonify({"error": "Base d'origine non supportée"}), 400
    except ValueError:
        return jsonify({"error": "La base d'origine doit être un entier"}), 400

    # Validation des caractères pour la base d'origine
    valid_chars = {
        2: set('01'),
        8: set('01234567'),
        10: set('0123456789'),
        16: set('0123456789abcdefABCDEF')
    }

    if not all(char in valid_chars[from_base] for char in input_value_str):
        return jsonify({"error": f"La valeur '{input_value_str}' contient des caractères invalides pour la base {from_base}"}), 400
        
    decimal_value, steps = to_decimal_steps(input_value_str, from_base)
    session["steps"] = steps

    if decimal_value is None:
        return jsonify({"error": f"Impossible de convertir '{input_value_str}' de la base {from_base} en décimal."}), 400

    results = {
        "binary": from_decimal(decimal_value, 2),
        "octal": from_decimal(decimal_value, 8),
        "decimal": from_decimal(decimal_value, 10),
        "hexadecimal": from_decimal(decimal_value, 16)
    }
    
    # Vérification si toutes les conversions ont réussi
    if any(val is None for val in results.values()):
        return jsonify({"error": "Erreur lors de la conversion vers l'une des bases de destination."}), 500

    session["last_input_value"] = input_value_str
    session["last_from_base"] = from_base

    return jsonify({
        "original_value": input_value_str,
        "original_base": from_base,
        "results": results,
        "error": None
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)