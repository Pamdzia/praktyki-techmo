import pandas as pd

data = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\datasets\nEMO\data.tsv', delimiter='\t')

# usuniecie rekordów z emocjami 'surprised' i 'fear'
data = data[~data['emotion'].isin(['surprised', 'fear'])]

# zmiana nazw emocji
emotion_map = {'anger': 'angry', 'happiness': 'happy', 'sadness': 'sad'}
data['emotion'] = data['emotion'].replace(emotion_map)

# nowy csv
data.to_csv('filtered_nEMO_all.csv', index=False)


# CSV RAVDESS
ravdess_data = pd.read_csv('dataset_info.csv')

emotions_to_keep = ['neutral', 'happy', 'angry', 'sad', 'fearful', 'disgust', 'surprised']
ravdess_data = ravdess_data[ravdess_data['Emotion'].isin(emotions_to_keep)]

# usunięcie niechciianych emocji
ravdess_data = ravdess_data[~ravdess_data['Emotion'].isin(['fearful', 'disgust', 'surprised'])]

ravdess_data.to_csv('filtered_RAVDESS_all.csv', index=False)
