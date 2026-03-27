# Script de nettoyage du CSV pour le projet ParisArchéo. A insérer plus tard dans le Notebook et dépôt Github.
# Le CSV "referentiel-archeologique-de-paris" présente un certain nombre d'erreurs, de valeurs nulles ou manquantes à nettoyer.
# CSV disponible ici : https://www.data.gouv.fr/datasets/referentiel-archeologique-de-paris (Open Data Commons Open Database License (ODbL)).

import pandas as pd
from pyproj import Transformer
import os

# 1.Chargement du dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
chemin = os.path.join(base_dir, "referentiel-archeologique-de-paris.csv")

df = pd.read_csv(chemin, sep=";", encoding="utf-8")

df.head()

###### NETTOYAGE ######

# 2.Suppression des colonnes inutiles (Commune, colonnes de périodes ("Antiquité", "Moyen-Âge"...) qui sont tout le temps vides).
# -> Le dataset ne comprends que des chantiers ayant eu lieu à Paris, inutile de garder cette colonne qui ne contient que la valeur "Paris".

colonnes_inutiles = [
    "Commune",
    "Préhistoire",
    "Protohistoire",
    "Antiquité",
    "Moyen-Age",
    "Temps modernes",
    "Epoque contemporaine"
]

df = df.drop(columns=colonnes_inutiles)

# 3. Renommage des colonnes.
# -> La base de données a pour nouvelle table principale "descriptifs_chantiers". Le dataset ne comporte qu'une liste de chantiers de fouilles.
# -> Toutes les données et noms de colonnes sont entièrement en français.

df = df.rename(columns={
    "Identifiant": "id_chantier",
    "Nature de l'opération": "nature_operation",
    "Responsable de l'opération": "responsable",
    "Date de l'opération": "date_operation",
    "Synthèse": "synthese"
})

# 4. Nouveau format des dates.
# -> PostgreSQL a été retenu pour la migration. Format de date : AAAA--MM-JJ (YYYY-MM-DD).

df["date_operation"] = pd.to_datetime(df["date_operation"], errors="coerce")

# 5.Nettoyage des colonnes : TEXT

df["nature_operation"] = df["nature_operation"].str.strip().str.lower()
df["responsable"] = df["responsable"].fillna("").str.strip().str.title()
df["synthese"] = df["synthese"].str.strip()

# 6. Colonne période.
# -> Plutôt que multiples colonnes par période (qui sont vides dans le CSV), utiliser une colonne unique (vide au départ).
# -> La colonne pourra être remplie ultérieurement.

df["periode"] = None

###### CREATION DES TABLES SUPPLEMENTAIRES #######

# 7. Table "Localisation".
# -> Les colonnes latitude/longitude s'appellement originellement dans le CSV X/Y. A renommer.

transformer = Transformer.from_crs("EPSG:2154", "EPSG:4326", always_xy=True)
df["longitude"], df["latitude"] = transformer.transform(df["X"], df["Y"])

# "id_chantier" reprends les valeurs de la colonne "Identifiant".

localisation = df[[
    "id_chantier",
    "Adresse",
    "Code postal",
    "latitude",
    "longitude"
]].copy()

localisation = localisation.rename(columns={
    "Adresse": "adresse",
    "Code postal": "code_postal"
})

###### Export final ###

df.to_csv(os.path.join(base_dir, "descriptifs_chantiers_clean.csv"), index=False)
localisation.to_csv(os.path.join(base_dir, "localisation_clean.csv"), index=False)