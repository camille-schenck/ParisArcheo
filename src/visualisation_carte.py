import pandas as pd
import folium
from folium.plugins import MarkerCluster

## Chargement + fusion des données
## descriptifs_chantiers_clean.csv + localisation_clean.csv

try:
    df = pd.read_csv(r"C:\Users\camil\OneDrive\Documents\DOCUMENTS\DOCUMENTS_CODE\CODE_PROJETS EN COURS\PYTHON_PROJET EN COURS\ParisArcheo\src\descriptifs_chantiers_clean.csv")
    loc = pd.read_csv(r"C:\Users\camil\OneDrive\Documents\DOCUMENTS\DOCUMENTS_CODE\CODE_PROJETS EN COURS\PYTHON_PROJET EN COURS\ParisArcheo\src\localisation_clean.csv")

except:
    print("Fichiers non trouvés. Merci de réessayer ou de donner un autre chemin d'accès.")

## Fusion et renommage des colonnes
data = df.merge(loc, on = "id_chantier", how = "left")
data = data.rename(columns = {
    "latitude_y": "latitude",
    "longitude_y": "longitude"
})

## Zone géographique couverte par la carte (Paris intra-muros uniquement)

data = data[
    (data["latitude"] >= 48.815) &
    (data["latitude"] <= 48.902) &
    (data["longitude"] >= 2.224) &
    (data["longitude"] <= 2.469)
]

## Couleurs utilisées pour la carte

type_colors = {
    "découverte_ancienne": "darkred",
    "diagnostic": "blue",
    "fouille": "green",
    "surveillance": "orange",
    "autre": "gray"
}

def get_color(t):

    t = str(t).lower()
    
    for key in type_colors:
        if key in t:
            return type_colors[key]
    return "gray"


## Version bilingue (FR & EN)

def make_popup(row):
    
    fr = f"""
    <b>Adresse :</b> {row['adresse']}<br>
    <b>Type :</b> {row['nature_operation']}<br>
    <b>Date :</b> {row['date_operation']}<br>
    <b>Responsable :</b> {row['responsable']}<br>
    <b>Synthèse :</b> {row['synthese']}
    """

    ## Pour une éventuelle version anglaise, traduire la colonne "Synthèse" (les données ne sont pour l'instant qu'en français.)
    
    #en = f"""
    #<b>Address:</b> {row['adresse']}<br>
    #<b>Type:</b> {row['nature_operation']}<br>
    #<b>Date:</b> {row['date_operation']}<br>
    #<b>Supervisor:</b> {row['responsable']}<br>
    #<b>Summary:</b> {row['synthese']}
    #"""

    return folium.Popup(
        f"<h4>FR</h4>{fr}",
        #<hr><h4>EN</h4>{en}
        max_width=350
    )

## Création de la carte

m = folium.Map(
    localiion = [48.8566, 2.3522],
    zoom_start = 12,
    tiles = "CartoDB positron"
)

cluster = MarkerCluster().add_to(m)

## Marqueurs

for _, row in data.iterrows():

    if pd.notnull(row["latitude"]) and pd.notnull(row["longitude"]):
        folium.Marker(
            location = [row["latitude"], row["longitude"]],
            popup = make_popup(row),
            icon = folium.Icon(color = get_color(row["nature_operation"]))
        ).add_to(cluster)

## Affichage de la carte

m

## Sauvegarde HTML (nécessaire pour data.gouv)

m.save("parisarcheo_map.html")