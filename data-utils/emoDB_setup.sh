#!/bin/bash

# Skrypt bash uruchamiający skrypt Python z opcjonalnymi argumentami tak aby ustawić zapis danych pod wygodę uzytkownika

# Opcjonalne ścieżki jako argumenty
emoDB_PATH=${1:-"../downloaded_data/emoDB"} #Sciezka gdzie zapisujemy rozpakowany zbior danych ravdess

FEATURES_ALL_PATH=$"../four_emotions_csvs_all" #Sciezka do zapisu pelnych plikow csv z wyodrebnionymi features
FEATURES_SET_PATH=$"../four-emotions-csv-sets" #SCiezka do zapisu setów danych z wyodrebnionymi features

# Uruchomienie skryptu Python do tworzenia pliku CSV
python3 emoDB_csv_setter.py --base_directory "$emoDB_PATH"

# Uruchomienie skryptu Python do przetwarzania plików nEMO i RAVDESS
python3 emoDB_four_emotions_dataset_setup.py --emodb_path "$emoDB_PATH/emoDB.csv"

# Uruchomienie skryptu Python do ekstrakcji cech dla RAVDESS
python3 four_emotions_features_setup.py --base_path "$emoDB_PATH" --csv_path "../data-utils/four_emotions_emoDB.csv" --output_dir "$FEATURES_ALL_PATH"

# Uruchomienie skryptu Python do podziału danych na zbiory treningowy, walidacyjny i testowy dla RAVDESS
python3 four_emotions_data_division.py --csv_path "$FEATURES_ALL_PATH/four_emotions_emoDB_features.csv" --output_dir "$FEATURES_SET_PATH"
