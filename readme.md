# Convertisseur de bases numériques

Hello, voici mon mini-projet qui est un outil web interactif pour converir des nombres entre différentes bases numériques : Binaire (Base 2), Octal (Base 8), Décimal (Base 10) et Hexadécimal (Base 16).

L'application est construite avec Flask pour le backend et du JavaScript vanilla pour le frontend.

## Origine

J'ai commencé à apprendre l'électronique numérique en 3ème des humanités où j'ai appris à faire des conversions entre base numérique, au début ça semblait assez facile parcequ'on faisait des conversions des petits nombres, et au fur et mesure qu'on avançait, ça devenait encore plus complexe et long à converir avec des gros nombres. Et quelques années après avoir être initié à l'algorithme et la programmation, j'ai eu à repenser à ce problème mais sur un axe algorithme, et je me suis dit de créer un outil informatique qui facilitera la conversion basique des bases numériques.

## Fonctionnalités

Par rapport aux fonctionnalités, j'ai mis encore les fonctionnalités de base étant donnée que c'est une première version, mais je compte en ajouter ou améliorer certaines fonctionnalités
Parmi mes fonctionnalités, il y a :

* **Sélection de la Base d'origine :** L'utilisateur à la possibilité de choisir facilement entre Binaire, Octal, Décimal, ou Hexadécimal comme base pour le nombre d'entrée, celui qui servirade conversion

* **Saisie intelligence :** Le champ de saisie s'active après la sélection d'une base et adapte son comportement :
  * **Binaire :** N'accepte que les caractères '0' et '1'
  * **Octal :** N'accepte que les caractères de '0' à '1'
  * **Décimal :** N'accepte que les catractères de '0' à '9'
  * **Hexadécial :** N'accepte que les caractères de '0' à '9' et de 'a' à 'f'

* **Validation en temps réel :** Le programme envoie aux utilisateurs des indications immédiates s'ils saisissent un caractère non valide pour la base sélectionnée. Par exemple, un utilisateur choisi la base 8 mais il saisit 8 ou 9, le système vas l'envoyer un message d'erreur en temps réel.

* **Conversion en temps réel :** Le programme envoie les résultats de laconversion dans kes quatres bases (Binaire, octal, décimal et hexadécimal) après qu'un utilisateur aie cliqué sur le bouton 'convertir'

* **Affichage clair des résultats :** Les valeurs converties sont présentées de manière distincte et lisible

* **Effaçage du contenu dans le champs de saisi :** Le programme inclut également une fonctionnalité qui vas permettre aux utilisateurs de réinitialiser facilement le camp de saisie et les résultats aussi
* **Responsive design** : Comme toute application présentes en ligne sur le web est affichable dans tout les types d'écran à savoir : Ordinateur, téléphones, tablette ou même télévision. Et mon site est aussi responsif
* **Backend API avec Flask :** La logique de conversion est gérée par une API Flask que j'ai crée

## Technologies

* **Frontend**
  * HTML5
  * CSS3
  * JavaScript(ES6+)
  * Bootstap 4.5
  * Font Awesome 6.5
  * Google Fonts (Poppins)
* **Backend**
  * Python 3.13.2
  * Flask 3.1.1

## Structure de mon projet

/ConvertBase
|------ static/
|   |------ css/
|   |   |------ style.css
|   |
|   |------ js/
|   |   |------- script.js
|   |
|   |------ images/
|   |   |------- logo.png
|   |   |
|   |   |------- fav-icon.png
|------- templates/
|   |------ index.html
|
|------ app.py
|

## Objectif du projet

ce projet vise à fournir un outil pratique et éducatif pour la conversion entre les bases numériques courantes.
Il démontre également l'intégration d'un frontend interactif avec une API bckend construite avec Flask.

## Installation et utilisation en locale

* Vous pouvez télécharger le projet en format zip ou le cloner avec la commande git clone et ensuite accéder à ce projet avec la commande cd
* Créer un environnement virtuel si cela n'est pas encore faire
'python -m venv venv'
`source venve/bin/activate` sur windows: `ven\SCripts\activate`
* Instalez les dépendances
Utilisez cette commande pour l'installer : `pip install -r requirements.txt`
* Exécutez l'application Flask
Utilisez la commande : `python app.py`
* Ouvrez votre navigateur et allez à l'adresse `http://127.0.0.1:5000/`

## Fonctionnalités futures posibles

* COnversion pour d'autres bases (par exemple, bas 4 ou encore 32)
* Affichage des étapes de calcul de la conversion
* Historique des conversions récentes (En utilisant le LocalStoage du navigateur)
* Options de copie individuelle pour chaque résultat converti

## COntribution

Les contributions, idées, apports de bugds, et propositions des futures fonctionnalités possible sont les bienvenus ! N'hésitez pas à ouvrir une issue

## Auteur

Projet réalisé par @Gauthier Shimatu (le Shimatologue)
