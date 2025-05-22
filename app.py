# Lien vers mon github   : https://github.com/gshimatu
# Auteur                 : Gauthier Shimatu (Le shimatologue)
# Nom du fichier         : app.py
# Date de création       : 2025-05-19 21:21:43
# Description            : Fichier principal de l'application Flask pour la conversion de bases numériques.
# Version                : 1.0


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

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
        
    decimal_value = to_decimal(input_value_str, from_base)

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