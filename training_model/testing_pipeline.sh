#!/bin/bash

# Ścieżka do skryptu Python
script_name="testing.py"

# Wyszukiwanie folderów i uruchamianie skryptu dla każdego eksperymentu
for experiment in */ ; do
    if [ -d "$experiment" ]; then
        echo "Uruchamianie eksperymentu dla folderu: $experiment"
        python "$script_name" "${experiment%/}" # Usuwa końcowy slash z nazwy folderu
    fi
done

echo "Wszystkie eksperymenty zostały przetworzone."
