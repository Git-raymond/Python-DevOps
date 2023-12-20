#!/bin/bash

# Vérifier si des paramètres ont été passés
if [ $# -eq 0 ]; then
  echo "Aucun paramètre n'a été passé lors de l'exécution du script."
else
  echo "Les paramètres passés lors de l'exécution du script sont :"
  
  # Afficher tous les paramètres un par un
  for param in "$@"; do
    echo "$param"
  done
fi
