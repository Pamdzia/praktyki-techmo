#!/bin/bash

# ścieżka do skryptu Python
script_name="testing.py"

# lista dataset-ów
datasets=("RAVDESS" "nEMO")

# wyszukiwanie folderów i uruchamianie skryptu dla każdego eksperymentu i datasetu
for experiment in */ ; do
    if [ -d "$experiment" ]; then
        for dataset in "${datasets[@]}"; do
            experiment_name="${experiment%/}"
            echo "Uruchamianie eksperymentu dla folderu: $experiment_name i datasetu: $dataset"
            python "$script_name" "$dataset" "$experiment_name"
        done
    fi
done

echo "Wszystkie eksperymenty zostały przetworzone."
