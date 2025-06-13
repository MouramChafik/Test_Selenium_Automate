# Test Automation Project

Ce projet contient des tests automatisés pour l'interface d'administration d'une application e-commerce.

## Structure du Projet

```
.
├── config/
│   └── __init__.py      # Configuration et sélecteurs
├── tests/
│   ├── test_test_login_admin.py
│   ├── test_test_add_product.py
│   ├── test_test_edit_product.py
│   └── test_test_delete_product.py
└── README.md
```

## Tests Implémentés

### 1. Login Admin
- Vérifie la connexion à l'interface d'administration
- Valide les champs de connexion et le bouton de soumission

### 2. Ajout de Produit
- Teste l'ajout d'un nouveau produit
- Vérifie tous les champs requis (nom, SKU, prix, etc.)
- Gère l'upload d'image et l'éditeur de description riche

### 3. Édition de Produit
- Teste la modification d'un produit existant
- Vérifie la mise à jour des champs
- Gère l'éditeur de description riche

### 4. Suppression de Produit
- Teste la suppression d'un produit
- Vérifie la sélection via checkbox
- Confirme la suppression via la modale
- Rafraîchit la page pour vérifier la suppression

## Prérequis

- Python 3.13+
- Chrome Browser
- ChromeDriver (géré automatiquement via webdriver-manager)

## Installation

1. Cloner le repository
2. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Unix/macOS
   # ou
   .venv\Scripts\activate  # Sur Windows
   ```
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Exécution des Tests

Pour exécuter tous les tests :
```bash
pytest
```

Pour exécuter un test spécifique :
```bash
pytest tests/test_test_delete_product.py -v
```

## Notes Importantes

- Les tests utilisent Selenium WebDriver en mode headless
- Les sélecteurs CSS sont centralisés dans `config/__init__.py`
- Les tests incluent des attentes explicites pour la stabilité
- La suppression de produit inclut un rafraîchissement de page pour vérifier la suppression

## Structure des Tests

Chaque test suit une structure similaire :
1. Configuration du WebDriver
2. Login à l'interface admin
3. Navigation vers la section appropriée
4. Exécution de l'action (ajout/édition/suppression)
5. Vérification du résultat
6. Nettoyage (fermeture du navigateur)

## Configuration

Le fichier `config.py` contient :
- Les URLs de l'application
- Les identifiants de connexion
- Les sélecteurs CSS pour les éléments de l'interface
- Les temps d'attente
- La configuration du WebDriver

## Tests Disponibles

### 1. Tests de Connexion (`test_test_login_admin.py`)

Teste les scénarios de connexion :
- Connexion réussie avec des identifiants valides
- Tentative de connexion avec des identifiants invalides

### 2. Tests d'Ajout de Produit (`test_test_add_product.py`)

Teste le processus complet d'ajout d'un produit :
- Connexion à l'admin
- Navigation vers la page d'ajout de produit
- Remplissage des informations de base :
  - Nom du produit
  - SKU (unique, généré dynamiquement)
  - Prix
  - Poids
- Upload d'image
- Sélection de catégorie
- Configuration des informations SEO :
  - URL key
  - Meta title
  - Meta keywords
  - Meta description
- Configuration du statut et de la visibilité
- Configuration de l'inventaire
- Configuration des attributs
- Sauvegarde et vérification

### 3. Tests d'ajout de catégorie

Le test `test_test_add_category_form.py` vérifie le processus complet d'ajout d'une catégorie dans l'interface d'administration :

1. Connexion à l'interface d'administration
2. Navigation vers la page des catégories
3. Création d'une nouvelle catégorie avec :
   - Nom de la catégorie
   - Sélection d'une catégorie parente
   - URL key unique
   - Meta title, keywords et description
   - Upload d'une image
   - Vérification des boutons radio (status, include in nav, show products)
4. Sauvegarde de la catégorie et vérification du message de succès

Pour exécuter le test :
```bash
pytest tests/test_test_add_category_form.py -v
```

## Exécution des Tests

Pour exécuter tous les tests :
```bash
pytest -v
```

Pour exécuter un test spécifique :
```bash
pytest test_test_login_admin.py -v
pytest test_test_add_product.py -v
```

## Temps d'Exécution

- Test de connexion : ~12 secondes
- Test d'ajout de produit : ~81 secondes

## Fonctionnalités Spéciales

1. **Gestion des Attentes**
   - Utilisation de `WebDriverWait` pour les éléments dynamiques
   - Délais configurables entre les actions

2. **Upload d'Images**
   - Gestion automatique de l'upload d'images
   - Vérification de l'aperçu
   - Utilisation d'une image de test

3. **Génération de SKU Unique**
   - Création de SKU uniques basés sur le timestamp
   - Évite les conflits lors de tests multiples

4. **Gestion des Catégories**
   - Sélection de catégorie via une modale
   - Recherche de catégorie
   - Fermeture automatique de la modale

## Bonnes Pratiques Implémentées

1. **Fixtures Pytest**
   - Gestion automatique du WebDriver
   - Nettoyage des ressources après les tests

2. **Gestion des Erreurs**
   - Messages d'erreur détaillés
   - Logs de débogage
   - Tentatives de récupération

3. **Sélecteurs Robustes**
   - Utilisation de sélecteurs CSS stables
   - Attentes explicites pour les éléments dynamiques

4. **Modularité**
   - Fonctions helper réutilisables
   - Configuration centralisée
   - Tests indépendants

## Développement Futur

Scénarios de test à ajouter :
- [ ] Test avec champs obligatoires manquants
- [ ] Test avec image invalide
- [ ] Test avec valeurs limites
- [ ] Test de suppression d'image
- [ ] Test de modification de produit
- [ ] Test de suppression de produit

## Support

Pour toute question ou problème, veuillez créer une issue dans le repository. 