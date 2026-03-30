# ParisArcheo  
### Analyse et structuration du Référentiel archéologique de Paris  
### Analysis and Structuring of the Paris Archaeological Reference Dataset

---

## 🇫🇷 Présentation  
ParisArcheo est un projet d’analyse, de nettoyage et de structuration du **Référentiel archéologique de Paris**, un corpus patrimonial publié sur data.gouv.fr.  
L’objectif est de rendre ces données **fiables, lisibles et exploitables**, notamment en vue d’une migration vers **PostgreSQL/PostGIS**.

## 🇬🇧 Overview  
ParisArcheo is a project focused on analysing, cleaning, and structuring the **Paris Archaeological Reference Dataset**, published on data.gouv.fr.  
The goal is to make the data **reliable, readable, and usable**, especially in preparation for a migration to **PostgreSQL/PostGIS**.

---

## Objectifs / Objectives
- Normaliser et nettoyer les données (dates, typologies, périodes, localisation).  
- Diagnostiquer la qualité documentaire du corpus.  
- Identifier les tendances patrimoniales (typologies, périodes, géodonnées).  
- Préparer une base relationnelle moderne.

- Normalize and clean the data (dates, typologies, periods, location).  
- Assess the dataset’s documentary quality.  
- Identify heritage-related patterns (typologies, periods, geodata).  
- Prepare a modern relational database structure.

---

## Technologies
- Python (pandas, pyproj)  
- Jupyter Notebook  
- PostgreSQL + PostGIS  
- DBeaver  

---

## Contenu du dépôt / Repository Structure
- `notebook/` → Analyse complète + pipeline  
- `data/` → Dataset brut + versions nettoyées  
- `sql/` → Scripts SQL (vues, géométrie, index)  
- `README.md` → Présentation du projet  

- `notebook/` → Full analysis + processing pipeline  
- `data/` → Raw dataset + cleaned versions  
- `sql/` → SQL scripts (views, geometry, indexes)  
- `README.md` → Project overview  

---

## Résultats clés / Key Findings
- Colonnes de périodes vides → reconstruction nécessaire.  
- Typologies peu discriminantes → normalisation recommandée.  
- Forte hétérogénéité des descriptions.  
- Données spatiales normalisées et converties en géométrie PostGIS.

- Period columns empty → reconstruction required.  
- Typologies not granular enough → normalization recommended.  
- Strong variability in descriptive fields.  
- Spatial data normalized and converted to PostGIS geometry.

---

## Recommandations / Recommendations
- Créer une liste contrôlée des périodes historiques.  
- Normaliser les typologies et les champs sensibles.  
- Vérifier et harmoniser les données spatiales.  
- Documenter les choix de nettoyage.

- Create a controlled vocabulary for historical periods.  
- Normalize typologies and sensitive fields.  
- Validate and harmonize spatial data.  
- Document all cleaning and structuring decisions.

---

## Dataset
**Source :** https://www.data.gouv.fr/datasets/referentiel-archeologique-de-paris  
**Licence :** ODbL  
**Lignes :** 2279  
**Format :** CSV
** Note: The dataset included in this project is published under the ODbL license (Open Database License) by data.gouv.fr.
The MIT License applies only to the code and documentation created for this project.  

**Source:** https://www.data.gouv.fr/datasets/referentiel-archeologique-de-paris  
**License:** ODbL  
**Rows:** 2279  
**Format:** CSV  

---

Projet réalisé par **Camille — Ingénieure des données patrimoniales**  
Project by **Camille — Heritage Data Engineer**
