import os
import pandas as pd
import argparse

# Argumenty wiersza poleceń
parser = argparse.ArgumentParser(description='Przetwarzanie pliku EmoDB.')
parser.add_argument('--emodb_path', default='../downloaded_data/emoDB/emoDB.csv', help='Ścieżka do pliku EmoDB')

args = parser.parse_args()

# Ścieżka do pliku EmoDB
emodb_path = args.emodb_path

# Wczytywanie danych EmoDB
emodb_data = pd.read_csv(emodb_path)

# Mapa emocji do znormalizowanej formy
emotion_map = {
    'sadness': 'sad',
    'anger': 'angry',
    'happiness': 'happy',
    'neutral': 'neutral'
}

# Filtracja i mapowanie emocji
emodb_data_filtered = emodb_data[emodb_data['emotion'].isin(emotion_map.keys())].copy()
emodb_data_filtered.loc[:, 'emotion'] = emodb_data_filtered['emotion'].map(emotion_map)

# Dodawanie prefiksu "wav/" do kolumny 'relative path'
emodb_data_filtered['relative path'] = 'wav/' + emodb_data_filtered['relative path'].astype(str)

# Ścieżka do zapisu przefiltrowanych danych
output_path = os.path.join(os.getcwd(), 'four_emotions_emoDB.csv')

# Zapis przefiltrowanych danych do nowego pliku CSV
emodb_data_filtered.to_csv(output_path, index=False)

print("Plik EmoDB został przetworzony i zapisany do:", output_path)
