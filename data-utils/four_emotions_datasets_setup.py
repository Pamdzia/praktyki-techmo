import os
import pandas as pd

# SCIEZKIII
default_nemo_path = r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\downloaded_data\nEMO\nEMO-main\data.tsv'
default_ravdess_song_path = r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\downloaded_data\RAVDESS\audio_song.csv'
default_ravdess_speech_path = r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\downloaded_data\RAVDESS\audio_speech.csv'

# sciezki beda ze zmienych srodowiskowych o ile sa ustawione
nemo_path = os.getenv('NEMO_PATH', default_nemo_path)
ravdess_song_path = os.getenv('RAVDESS_SONG_PATH', default_ravdess_song_path)
ravdess_speech_path = os.getenv('RAVDESS_SPEECH_PATH', default_ravdess_speech_path)

nemo_data = pd.read_csv(nemo_path, delimiter='\t')
ravdess_song_data = pd.read_csv(ravdess_song_path)
ravdess_speech_data = pd.read_csv(ravdess_speech_path)

# przetwarzanie pliku nEMO
nemo_data = nemo_data[~nemo_data['emotion'].isin(['surprised', 'fear'])]
emotion_map = {'anger': 'angry', 'happiness': 'happy', 'sadness': 'sad'}
nemo_data['emotion'] = nemo_data['emotion'].replace(emotion_map)

nemo_data = nemo_data[['file_id', 'emotion', 'speaker_id', 'gender']]
nemo_data.columns = ['relative path', 'emotion', 'actor', 'gender']

# przetwarzanie plików RAVDESS
emotions_to_keep = ['neutral', 'happy', 'angry', 'sad']

ravdess_song_data = ravdess_song_data[ravdess_song_data['Emotion'].isin(emotions_to_keep)]
ravdess_speech_data = ravdess_speech_data[ravdess_speech_data['Emotion'].isin(emotions_to_keep)]

ravdess_song_data = ravdess_song_data[['Relative Path', 'Emotion', 'Actor', 'Gender']]
ravdess_song_data.columns = ['relative path', 'emotion', 'actor', 'gender']
ravdess_song_data['gender'] = ravdess_song_data['gender'].str.lower()

ravdess_speech_data = ravdess_speech_data[['Relative Path', 'Emotion', 'Actor', 'Gender']]
ravdess_speech_data.columns = ['relative path', 'emotion', 'actor', 'gender']
ravdess_speech_data['gender'] = ravdess_speech_data['gender'].str.lower()

# połączenie plików RAVDESS
ravdess_combined = pd.concat([ravdess_song_data, ravdess_speech_data])

# zapis
nemo_data.to_csv('four_emotions_nEMO.csv', index=False)
ravdess_combined.to_csv('four_emotions_RAVDESS.csv', index=False)

print("Pliki zostały przetworzone i zapisane.")
