# logs_cleanup.py

import os
import time

def cleanup_logs(logs_directory, days_to_keep):
    current_time = time.time()

    for file in os.listdir(logs_directory):
        file_path = os.path.join(logs_directory, file)
        if os.path.isfile(file_path):
            # Calculer la différence en jours entre le temps actuel et le temps de création du fichier
            file_age = (current_time - os.path.getctime(file_path)) / (24 * 3600)

            # Supprimer les fichiers plus anciens que la période spécifiée
            if file_age > days_to_keep:
                os.remove(file_path)
                print(f"Removed old log file: {file_path}")

if __name__ == "__main__":
    logs_directory = "/var/log"  # Change this to your log directory
    days_to_keep = 10

    cleanup_logs(logs_directory, days_to_keep)
