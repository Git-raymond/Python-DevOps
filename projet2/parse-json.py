import os
import json

def parse_json(file_path):
    # Déterminer et afficher le chemin du fichier JSON
    print(f"Chemin du fichier JSON : {file_path}")

    # Créer un chemin absolu vers le fichier JSON
    absolute_path = os.path.abspath(file_path)
    print(f"Chemin absolu du fichier JSON : {absolute_path}")

    # Lire et analyser le fichier JSON
    with open(file_path, 'r') as file:
        json_content = json.load(file)

    # Extrait et affiche la valeur associée à la clé 'name' dans le fichier JSON
    name_value = json_content.get('name')
    print(f"Valeur associée à la clé 'name' : {name_value}")

    # Parcourt toutes les clés et valeurs du dictionnaire JSON, affichant chaque paire clé-valeur
    print("Paires clé-valeur dans le fichier JSON:")
    for key, value in json_content.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Chemin du fichier JSON
    json_file_path = "/home/formation/TP1/Python-DevOPs/projet2/Files/exemple.json"

    # Appel de la fonction pour analyser le fichier JSON
    parse_json(json_file_path)
