/*
 * Lien vers mon github   : https://github.com/gshimatu
 * Auteur                 : Gauthier Shimatu (Le shimatologue)
 * Nom du fichier         : script.js
 * Date de création       : 2025-05-19 21:20:55
 * Description            : Fichier JavaScript pour la conversion de bases numériques
 * Version                : 1.0
 */


document.addEventListener('DOMContentLoaded', () => {
    const inputValueField = document.getElementById('inputValue');
    const inputErrorField = document.getElementById('inputError');
    const selectedBaseInfoField = document.getElementById('selectedBaseInfo');

    const baseButtons = document.querySelectorAll('.base-btn');
    const convertBtn = document.getElementById('convertBtn');
    const clearBtn = document.getElementById('clearBtn');

    const resultBinary = document.getElementById('resultBinary');
    const resultOctal = document.getElementById('resultOctal');
    const resultDecimal = document.getElementById('resultDecimal');
    const resultHexadecimal = document.getElementById('resultHexadecimal');

    let currentBase = null;
    let currentPattern = null;

    document.getElementById('currentYear').textContent = new Date().getFullYear();

    baseButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Reset active state for all buttons
            baseButtons.forEach(btn => btn.classList.remove('active'));
            // Set active state for clicked button
            button.classList.add('active');

            currentBase = parseInt(button.dataset.base);
            currentPattern = new RegExp(button.dataset.pattern);
            
            inputValueField.readOnly = false;
            inputValueField.placeholder = button.dataset.placeholder;
            inputValueField.value = ''; 
            clearResults();
            inputErrorField.classList.add('d-none');
            inputErrorField.textContent = '';
            selectedBaseInfoField.textContent = `Base sélectionnée : ${getBaseName(currentBase)}. Caractères autorisés : ${getAllowedChars(currentBase)}`;
            inputValueField.focus();
        });
    });

    inputValueField.addEventListener('input', () => {
        if (!currentBase || !currentPattern) {
            showError("Veuillez d'abord sélectionner une base d'origine.");
            inputValueField.value = '';
            return;
        }

        const value = inputValueField.value;
        if (value === '') {
            hideError();
            return;
        }

        if (!currentPattern.test(value)) {
            // Filter out invalid characters
            let filteredValue = '';
            for (let char of value) {
                if (new RegExp(`^[${getAllowedChars(currentBase, true)}]$`, 'i').test(char)) {
                    filteredValue += char;
                }
            }
            inputValueField.value = filteredValue;
            showError(`Caractère invalide pour la base ${getBaseName(currentBase)}. Caractères autorisés : ${getAllowedChars(currentBase)}`);
        } else {
            hideError();
        }
    });

    convertBtn.addEventListener('click', async () => {
        const value = inputValueField.value.trim();

        if (!currentBase) {
            showError("Veuillez sélectionner une base d'origine.");
            return;
        }
        if (value === '') {
            showError("Veuillez entrer une valeur à convertir.");
            return;
        }
        if (!currentPattern.test(value)) {
            showError(`La valeur n'est pas valide pour la base ${getBaseName(currentBase)}.`);
            return;
        }

        hideError();
        convertBtn.disabled = true;
        convertBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Conversion...';

        try {
            const response = await fetch('/api/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ value: value, from_base: currentBase }),
            });

            const data = await response.json();

            if (response.ok && !data.error) {
                resultBinary.textContent = data.results.binary;
                resultOctal.textContent = data.results.octal;
                resultDecimal.textContent = data.results.decimal;
                resultHexadecimal.textContent = data.results.hexadecimal.toUpperCase();
            } else {
                showError(data.error || "Erreur lors de la conversion.");
                clearResults();
            }
        } catch (error) {
            console.error("Erreur d'appel API:", error);
            showError("Erreur de communication avec le serveur.");
            clearResults();
        } finally {
            convertBtn.disabled = false;
            convertBtn.innerHTML = '<i class="fas fa-exchange-alt"></i> Convertir';
        }
    });

    clearBtn.addEventListener('click', () => {
        inputValueField.value = '';
        // inputValueField.readOnly = true; // Optionnel: re-bloquer le champ
        // inputValueField.placeholder = "Sélectionnez une base pour commencer";
        // baseButtons.forEach(btn => btn.classList.remove('active'));
        // currentBase = null;
        // currentPattern = null;
        // selectedBaseInfoField.textContent = '';
        hideError();
        clearResults();
    });

    function showError(message) {
        inputErrorField.textContent = message;
        inputErrorField.classList.remove('d-none');
        inputValueField.classList.add('is-invalid');
    }

    function hideError() {
        inputErrorField.classList.add('d-none');
        inputErrorField.textContent = '';
        inputValueField.classList.remove('is-invalid');
    }

    function clearResults() {
        resultBinary.textContent = '-';
        resultOctal.textContent = '-';
        resultDecimal.textContent = '-';
        resultHexadecimal.textContent = '-';
    }
    
    function getBaseName(base) {
        switch(base) {
            case 2: return 'Binaire';
            case 8: return 'Octale';
            case 10: return 'Décimale';
            case 16: return 'Hexadécimale';
            default: return 'Inconnue';
        }
    }

    function getAllowedChars(base, forRegexCharClass = false) {
        switch(base) {
            case 2: return '01';
            case 8: return '0-7';
            case 10: return '0-9';
            case 16: return forRegexCharClass ? '0-9a-fA-F' : '0-9, a-f, A-F';
            default: return '';
        }
    }

});