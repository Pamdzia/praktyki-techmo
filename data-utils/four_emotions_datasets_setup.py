import os
import pandas as pd
import argparse

# Argumenty wiersza poleceń
parser = argparse.ArgumentParser(description='Przetwarzanie plików nEMO i RAVDESS.')
parser.add_argument('--nemo_path', default='../downloaded_data/nEMO/nEMO-main/data.tsv', help='Ścieżka do pliku nEMO')
parser.add_argument('--ravdess_song_path', default='../downloaded_data/RAVDESS/audio_song.csv', help='Ścieżka do pliku RAVDESS audio song')
parser.add_argument('--ravdess_speech_path', default='../downloaded_data/RAVDESS/audio_speech.csv', help='Ścieżka do pliku RAVDESS audio speech')

args = parser.parse_args()

# Ścieżki
nemo_path = args.nemo_path
ravdess_song_path = args.ravdess_song_path
ravdess_speech_path = args.ravdess_speech_path

nemo_data = pd.read_csv(nemo_path, delimiter='\t')
ravdess_song_data = pd.read_csv(ravdess_song_path)
ravdess_speech_data = pd.read_csv(ravdess_speech_path)

# Przetwarzanie pliku nEMO
nemo_data = nemo_data[~nemo_data['emotion'].isin(['surprised', 'fear'])]
emotion_map = {'anger': 'angry', 'happiness': 'happy', 'sadness': 'sad'}
nemo_data['emotion'] = nemo_data['emotion'].replace(emotion_map)

nemo_data = nemo_data[['file_id', 'emotion', 'speaker_id', 'gender']]
nemo_data.columns = ['relative path', 'emotion', 'actor', 'gender']

# Przetwarzanie plików RAVDESS
emotions_to_keep = ['neutral', 'happy', 'angry', 'sad']

ravdess_song_data = ravdess_song_data[ravdess_song_data['Emotion'].isin(emotions_to_keep)]
ravdess_speech_data = ravdess_speech_data[ravdess_speech_data['Emotion'].isin(emotions_to_keep)]

ravdess_song_data = ravdess_song_data[['Relative Path', 'Emotion', 'Actor', 'Gender']]
ravdess_song_data.columns = ['relative path', 'emotion', 'actor', 'gender']
ravdess_song_data['gender'] = ravdess_song_data['gender'].str.lower()

ravdess_speech_data = ravdess_speech_data[['Relative Path', 'Emotion', 'Actor', 'Gender']]
ravdess_speech_data.columns = ['relative path', 'emotion', 'actor', 'gender']
ravdess_speech_data['gender'] = ravdess_speech_data['gender'].str.lower()

# Połączenie plików RAVDESS
ravdess_combined = pd.concat([ravdess_song_data, ravdess_speech_data])

# Zapis
nemo_data.to_csv('four_emotions_nEMO.csv', index=False)
ravdess_combined.to_csv('four_emotions_RAVDESS.csv', index=False)

print("Pliki zostały przetworzone i zapisane.")
