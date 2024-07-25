#!/bin/bash

# Skrypt bash uruchamiający skrypt Python z opcjonalnymi argumentami tak aby ustawić zapis danych pod wygodę uzytkownika

# Opcjonalne ścieżki jako argumenty
TESS_PATH=${1:-"../downloaded_data/TESS"} #Sciezka gdzie zapisujemy rozpakowany zbior danych ravdess

FEATURES_ALL_PATH=$"../four_emotions_csvs_all" #Sciezka do zapisu pelnych plikow csv z wyodrebnionymi features
FEATURES_SET_PATH=$"../four-emotions-csv-sets" #SCiezka do zapisu setów danych z wyodrebnionymi features

# Uruchomienie skryptu Python do tworzenia pliku CSV
python3 tess_csv_setter.py --base_directory "$TESS_PATH"

# Uruchomienie skryptu Python do przetwarzania plików nEMO i RAVDESS
python3 tess_four_emotions_dataset_setup.py --tess_path "$TESS_PATH/TESS.csv"

# Uruchomienie skryptu Python do ekstrakcji cech dla RAVDESS
python3 four_emotions_features_setup.py --base_path "$TESS_PATH" --csv_path "../data-utils/four_emotions_TESS.csv" --output_dir "$FEATURES_ALL_PATH"
