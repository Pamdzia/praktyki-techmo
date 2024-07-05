# Skrypt PowerShell uruchamiający skrypt Python z opcjonalnymi argumentami tak aby ustawić zapis danych pod wygodę użytkownika

# Opcjonalne ścieżki jako argumenty
$RAVDESS_PATH = if ($args.Count -gt 0) { $args[0] } else { "..\downloaded_data\RAVDESS" } # Ścieżka gdzie zapisujemy rozpakowany zbiór danych ravdess
$NEMO_PATH = if ($args.Count -gt 1) { $args[1] } else { "..\downloaded_data\nEMO" } # Ścieżka gdzie zapisujemy rozpakowany zbiór danych nemo
$ZIP_PATH = if ($args.Count -gt 2) { $args[2] } else { "..\downloaded_data\zip" } # Ścieżka gdzie pobierany zostaje zip z datasetami

$FEATURES_ALL_PATH = "..\four_emotions_csvs_all" # Ścieżka do zapisu pełnych plików csv z wyodrębnionymi cechami
$FEATURES_SET_PATH = "..\four-emotions-csv-sets" # Ścieżka do zapisu zestawów danych z wyodrębnionymi cechami

# Uruchomienie skryptu Python z argumentami opcjonalnymi
python data_downloader.py --ravdess_path "$RAVDESS_PATH" --nemo_path "$NEMO_PATH" --zip_path "$ZIP_PATH"

# Uruchomienie skryptu Python do tworzenia pliku CSV
python Ravdess_Csv_setter.py --base_directory "$RAVDESS_PATH"

# Uruchomienie skryptu Python do przetwarzania plików nEMO i RAVDESS
python four_emotions_datasets_setup.py --nemo_path "$NEMO_PATH\nEMO-main\data.tsv" --ravdess_song_path "$RAVDESS_PATH\audio_song.csv" --ravdess_speech_path "$RAVDESS_PATH\audio_speech.csv"

# Uruchomienie skryptu Python do ekstrakcji cech dla RAVDESS
python four_emotions_features_setup.py --base_path "$RAVDESS_PATH" --csv_path "..\data-utils\four_emotions_RAVDESS.csv" --output_dir "$FEATURES_ALL_PATH"

# Uruchomienie skryptu Python do ekstrakcji cech dla nEMO
python four_emotions_features_setup.py --base_path "$NEMO_PATH\nEMO-main\samples" --csv_path "..\data-utils\four_emotions_nEMO.csv" --output_dir "$FEATURES_ALL_PATH"

# Uruchomienie skryptu Python do podziału danych na zbiory treningowy, walidacyjny i testowy dla RAVDESS
python four_emotions_data_division.py --csv_path "$FEATURES_ALL_PATH\four_emotions_RAVDESS_features.csv" --output_dir "$FEATURES_SET_PATH"

# Uruchomienie skryptu Python do podziału danych na zbiory treningowy, walidacyjny i testowy dla nEMO
python four_emotions_data_division.py --csv_path "$FEATURES_ALL_PATH\four_emotions_nEMO_features.csv" --output_dir "$FEATURES_SET_PATH"
