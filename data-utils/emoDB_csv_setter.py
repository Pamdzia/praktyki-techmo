import os
import csv
import argparse

parser = argparse.ArgumentParser(description='Tworzenie pliku CSV z danymi EmoDB.')
parser.add_argument('--base_directory', default=r'../downloaded_data/emoDB', help='Podstawowy katalog EmoDB')

args = parser.parse_args()

base_directory = args.base_directory
wav_directory = os.path.join(base_directory, 'wav')

columns = ['relative path', 'actor', 'text code', 'emotion', 'version', 'gender']

# Mapa kodów emocji na emocje (bazując na literach z niemieckiego oznaczenia)
emotion_map = {
    'W': 'anger',        # Wut (anger)
    'L': 'boredom',      # Langeweile (boredom)
    'E': 'disgust',      # Ekel (disgust)
    'A': 'fear',         # Angst (fear)
    'F': 'happiness',    # Freude (happiness)
    'T': 'sadness',      # Trauer (sadness)
    'N': 'neutral'       # Neutral
}

# Funkcja dekodująca nazwę pliku
def decode_filename(filename):
    base_name = filename.split('.')[0]
    actor_id = base_name[:2]
    return {
        'actor': actor_id,
        'text code': base_name[2:5],
        'emotion': emotion_map.get(base_name[5], 'unknown'),
        'version': base_name[6:],
        'gender': 'female' if int(actor_id) % 2 == 0 else 'male'
    }

csv_path = os.path.join(base_directory, 'emoDB.csv')

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()

    for filename in os.listdir(wav_directory):
        if filename.endswith('.wav'):
            relative_path = filename
            details = decode_filename(filename)
            details['relative path'] = relative_path
            writer.writerow(details)

print("EmoDB dataset info is ready.")
