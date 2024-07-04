import os
import csv
import argparse

# Argumenty wiersza poleceń
parser = argparse.ArgumentParser(description='Tworzenie pliku CSV z danymi RAVDESS.')
parser.add_argument('--base_directory', default=r'../downloaded_data/RAVDESS', help='Podstawowy katalog RAVDESS')

args = parser.parse_args()

# Podstawowy katalog
base_directory = args.base_directory

columns = ['Relative Path', 'Modality', 'Vocal Channel', 'Emotion', 'Intensity', 'Statement', 'Repetition', 'Actor', 'Gender']

def decode_filename(filename):
    parts = filename.split('.')[0].split('-')
    return {
        'Modality': 'audio-only' if parts[0] == '03' else 'video-only',
        'Vocal Channel': 'speech' if parts[1] == '01' else 'song',
        'Emotion': {
            '01': 'neutral', '02': 'calm', '03': 'happy', '04': 'sad',
            '05': 'angry', '06': 'fearful', '07': 'disgust', '08': 'surprised'
        }[parts[2]],
        'Intensity': 'normal' if parts[3] == '01' else 'strong',
        'Statement': 'Kids are talking by the door' if parts[4] == '01' else 'Dogs are sitting by the door',
        'Repetition': '1st' if parts[5] == '01' else '2nd',
        'Actor': parts[6],
        'Gender': 'Male' if int(parts[6]) % 2 != 0 else 'Female'
    }

# Iterowanie przez podfoldery w base_directory
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    
    if os.path.isdir(folder_path):
        csv_filename = f'{folder_name}.csv'
        csv_path = os.path.join(base_directory, csv_filename)
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()

            for actor_id in range(1, 25):  
                actor_folder = f'Actor_{str(actor_id).zfill(2)}'
                actor_path = os.path.join(folder_path, actor_folder)
                
                if os.path.exists(actor_path):
                    for filename in os.listdir(actor_path):
                        if filename.endswith('.wav'):
                            relative_path = f'{folder_name}/{actor_folder}/{filename}'
                            details = decode_filename(filename)
                            details['Relative Path'] = relative_path
                            writer.writerow(details)

print("Ravdess dataset info is ready.")
