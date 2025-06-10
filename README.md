# Tests Automatisés pour l'Interface d'Administration

Ce projet contient des tests automatisés pour l'interface d'administration d'une application e-commerce, utilisant Selenium WebDriver et pytest.

## Prérequis

- Python 3.13 ou supérieur
- Chrome Browser
- pip (gestionnaire de paquets Python)

## Installation

1. Cloner le repository :
```bash
git clone [URL_DU_REPO]
cd [NOM_DU_DOSSIER]
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Structure du Projet

```
.
├── README.md
├── requirements.txt
├── config.py                 # Configuration et sélecteurs
├── test_test_login_admin.py  # Tests de connexion
└── test_test_add_product.py  # Tests d'ajout de produit
```

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