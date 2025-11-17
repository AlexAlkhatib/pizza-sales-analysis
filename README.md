# 🍕 **Pizza Sales Data Analysis — Nettoyage, Transformation & Visualisation**

Ce projet analyse des données de ventes de pizzas à partir de plusieurs fichiers (ventes, tailles, catégories…).
Il met en œuvre un large éventail de compétences Python pour explorer, nettoyer, manipuler, fusionner et visualiser les données.
L’objectif : comprendre les performances des pizzas (ventes, prix, quantités), détecter les tendances et préparer les données pour une analyse avancée.


## 🎯 Objectifs du projet

* Nettoyer, filtrer et inspecter un dataset de ventes de pizzas
* Fusionner plusieurs sources (ventes, taille, catégories)
* Effectuer des transformations et agrégations avancées
* Analyser les tendances de prix, quantités et catégories
* Manipuler le texte, les dates, les index et les structures pandas
* Générer des visualisations claires (boxplots, courbes, etc.)


## 🧰 Stack Technique

* **Python 3**
* **pandas** (manipulation et analyse de données)
* **Matplotlib** (visualisations)
* **Seaborn** (graphismes avancés)
* **datetime** pour filtrage des dates
* Fichiers **CSV** & **Excel** comme sources


## 📊 Données utilisées

* `pizza_sales.xlsx`
* `pizza_size.csv`
* `pizza_category.csv`
* Données complémentaires : `another_pizza_sales.xlsx`, `pizza_sales_voucher.xlsx`

Chaque fichier apporte des informations sur :

* les commandes
* les prix & quantités
* les tailles des pizzas
* les catégories
* les ingrédients


## 🧹 Étapes réalisées dans le projet

### 1. **Exploration du dataset**

* `head()`, `tail()`, `describe()`, `info()`
* Comptage des valeurs nulles
* Détection de doublons

### 2. **Sélection & manipulation des colonnes**

* Sélection par label (`loc`), slicing, extractions ciblées
* Sélection de lignes spécifiques
* Manipulation des index (`set_index`, `reset_index`)

### 3. **Troncature et slicing**

* `truncate()` sur lignes et séries
* Extraction de sous-ensembles

### 4. **Filtrage avancé**

* Conditions simples et multiples
* Filtrage par date (conversion `datetime`)
* Filtrage selon gammes de prix
* Logique `and` / `or`

### 5. **Gestion des valeurs manquantes**

* `dropna()`
* `fillna()` avec valeurs personnalisées

### 6. **Suppression de lignes et colonnes**

* `drop()` sur indices multiples
* Suppression de colonnes uniques ou multiples

### 7. **Tri et ordonnancement**

* Tri simple ou multi-critères (`sort_values`)
* Tri ascendant / descendant

### 8. **Agrégations & GroupBy**

* Comptages
* Sums, means
* Agrégation multiple via `agg()`
* Totaux par taille de pizza
* Quantités et prix par catégories

### 9. **Merging et concatenation**

* Fusion verticale & horizontale (`concat`)
* Fusion sur clé (`merge`)

### 10. **Manipulation de texte**

* Mise en minuscule/majuscule/titre
* Remplacement de texte
* Nettoyage des espaces


## 📈 Visualisation

### 📌 Boxplot des ventes par catégorie

```python
sns.boxplot(x='category', y='total_price', data=merged_df)
```

Permet d’analyser la distribution des prix selon le type de pizza.


## 📂 Structure du projet

```
pizza_sales_analysis/
 ├── pizza_sales.xlsx
 ├── pizza_size.csv
 ├── pizza_category.csv
 ├── another_pizza_sales.xlsx
 ├── pizza_sales_voucher.xlsx
 ├── pizza_sales_analysis.py      # Ton script principal
 └── README.md
```


## 🧠 Compétences démontrées

✔ Slicing, filtrage avancé et manipulation de DataFrames
✔ Gestion des valeurs manquantes & doublons
✔ Agrégations, groupements & statistiques descriptives
✔ Fusion multi-sources (CSV + Excel) via merge & concat
✔ Préparation des données pour analyse ou machine learning
✔ Nettoyage et transformation de texte
✔ Visualisation via Seaborn et Matplotlib
✔ Méthodologie d’analyse structurée appliquée à des données réelles


## 🔧 Pistes d’amélioration

* Ajouter des heatmaps ou analyses de corrélation
* Construire un dashboard Power BI / Tableau
* Ajouter des visualisations supplémentaires (tops ventes, tendances mensuelles)
* Créer une API ou un script CLI pour automatiser l’analyse
* Développer un modèle prédictif (ex : prévision de demande)


## 👤 À propos

Projet réalisé par **Alex Alkhatib** dans le cadre de mon apprentissage en data analysis & Python.


## 📄 Licence
MIT License
Copyright (c) 2025 Alex Alkhatib
