import os
import pandas as pd
import argparse

# Argumenty wiersza poleceń
parser = argparse.ArgumentParser(description='Przetwarzanie pliku TESS.')
parser.add_argument('--tess_path', default='../downloaded_data/TESS/TESS.csv', help='Ścieżka do pliku TESS')

args = parser.parse_args()

# Ścieżka do pliku TESS
tess_path = args.tess_path

# Wczytywanie danych TESS
tess_data = pd.read_csv(tess_path)

# Mapa emocji do znormalizowanej formy
emotion_map = {
    'angry': 'angry',
    'happy': 'happy',
    'sad': 'sad',
    'neutral': 'neutral'
}

# Filtracja i mapowanie emocji
tess_data_filtered = tess_data[tess_data['emotion'].isin(emotion_map.keys())].copy()
tess_data_filtered.loc[:, 'emotion'] = tess_data_filtered['emotion'].map(emotion_map)

# Dodawanie prefiksu "wav/" do kolumny 'relative path'
tess_data_filtered['relative path'] = 'dataverse_files/' + tess_data_filtered['relative path'].astype(str)

# Ścieżka do zapisu przefiltrowanych danych
output_path = os.path.join(os.getcwd(), 'four_emotions_TESS.csv')

# Zapis przefiltrowanych danych do nowego pliku CSV
tess_data_filtered.to_csv(output_path, index=False)

print("Plik TESS został przetworzony i zapisany do:", output_path)
