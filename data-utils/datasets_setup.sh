#!/bin/bash

# Skrypt bash uruchamiający skrypt Python z opcjonalnymi argumentami tak aby ustawić zapis danych pod wygodę uzytkownika

# Opcjonalne ścieżki jako argumenty
RAVDESS_PATH=${1:-"../downloaded_data/RAVDESS"} #Sciezka gdzie zapisujemy rozpakowany zbior danych ravdess
NEMO_PATH=${2:-"../downloaded_data/nEMO"} #Sciezka gdzie zapisujemy rozpakowany zbior danych nemo
ZIP_PATH=${3:-"../downloaded_data/zip"} #Sciezka gdzie pobierany zostaje zip z datasetami

FEATURES_ALL_PATH=$"../four_emotions_csvs_all" #Sciezka do zapisu pelnych plikow csv z wyodrebnionymi features
FEATURES_SET_PATH=$"../four-emotions-csv-sets" #SCiezka do zapisu setów danych z wyodrebnionymi features

# Uruchomienie skryptu Python z argumentami opcjonalnymi
python3 data_downloader.py --ravdess_path "$RAVDESS_PATH" --nemo_path "$NEMO_PATH" --zip_path "$ZIP_PATH"

# Uruchomienie skryptu Python do tworzenia pliku CSV
python3 Ravdess_Csv_setter.py --base_directory "$RAVDESS_PATH"

# Uruchomienie skryptu Python do przetwarzania plików nEMO i RAVDESS
python3 four_emotions_datasets_setup.py --nemo_path "$NEMO_PATH/nEMO-main/data.tsv" --ravdess_song_path "$RAVDESS_PATH/audio_song.csv" --ravdess_speech_path "$RAVDESS_PATH/audio_speech.csv"

# Uruchomienie skryptu Python do ekstrakcji cech dla RAVDESS
python3 four_emotions_features_setup.py --base_path "$RAVDESS_PATH" --csv_path "../data-utils/four_emotions_RAVDESS.csv" --output_dir "$FEATURES_ALL_PATH"

# Uruchomienie skryptu Python do ekstrakcji cech dla nEMO
python3 four_emotions_features_setup.py --base_path "$NEMO_PATH/nEMO-main/samples" --csv_path "../data-utils/four_emotions_nEMO.csv" --output_dir "$FEATURES_ALL_PATH"

# Uruchomienie skryptu Python do podziału danych na zbiory treningowy, walidacyjny i testowy dla RAVDESS
python3 four_emotions_data_division.py --csv_path "$FEATURES_ALL_PATH/four_emotions_RAVDESS_features.csv" --output_dir "$FEATURES_SET_PATH"

# Uruchomienie skryptu Python do podziału danych na zbiory treningowy, walidacyjny i testowy dla nEMO
python3 four_emotions_data_division.py --csv_path "$FEATURES_ALL_PATH/four_emotions_nEMO_features.csv" --output_dir "$FEATURES_SET_PATH"