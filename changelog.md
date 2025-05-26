# Changelog

## Version 2.0 – 2025-05-24

### Nouvelles fonctionnalités

- **Affichage détaillé des étapes de conversion** : Ajout d’une page dédiée permettant de visualiser les étapes de conversion pour chaque base cible (octal, décimal, hexadécimal) avec navigation par boutons.
- **Navigation dynamique des étapes** : Trois boutons permettent de choisir la base cible pour afficher les étapes correspondantes.
- **Restauration automatique** : Lorsqu’un utilisateur revient sur la page principale, la valeur saisie et les résultats précédents sont automatiquement restaurés.
- **Copie individuelle des résultats** : Ajout d’un bouton de copie à côté de chaque résultat pour copier individuellement la valeur convertie.
- **Bouton Effacer** : Réintégration du bouton pour réinitialiser le champ de saisie et les résultats.
- **Animation sur le bouton "Afficher étapes"** : Ajout d’une animation de chargement lors de l’accès à la page des étapes.
- **Sécurité améliorée** : Utilisation d’une variable d’environnement pour la clé secrète Flask (`SECRET_KEY`), retirée du code source public.

### Améliorations

- **Interface utilisateur** : Uniformisation du style et de l’ergonomie sur toutes les pages (index, étapes, footer).
- **Validation renforcée** : Meilleure gestion des erreurs et des caractères invalides selon la base sélectionnée.
- **Expérience utilisateur** : Les boutons sont désactivés/activés dynamiquement selon le contexte d’utilisation.

### Corrections

- Correction de bugs d’accessibilité HTML (structure des listes d’étapes).
- Correction de la restauration des résultats lors de la navigation entre les pages.  

---

**Auteur** : Gauthier Shimatu (Le Shimatologue)