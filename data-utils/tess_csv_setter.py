import os
import csv
import argparse

parser = argparse.ArgumentParser(description='Tworzenie pliku CSV z danymi TESS.')
parser.add_argument('--base_directory', default=r'../downloaded_data/TESS', help='Podstawowy katalog TESS')

args = parser.parse_args()

base_directory = args.base_directory
wav_directory = os.path.join(base_directory, 'dataverse_files')

columns = ['relative path', 'actor', 'word', 'emotion', 'gender']

# Funkcja dekodująca nazwę pliku
def decode_filename(filename):
    base_name = filename.split('.')[0]
    parts = base_name.split('_')
    speaker = parts[0]
    word = parts[1]
    emotion = parts[2]
    return {
        'actor': speaker,
        'word': word,
        'emotion': emotion,
        'gender': 'female'
    }

csv_path = os.path.join(base_directory, 'TESS.csv')

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()

    for filename in os.listdir(wav_directory):
        if filename.endswith('.wav'):
            relative_path = filename
            details = decode_filename(filename)
            details['relative path'] = relative_path
            writer.writerow(details)

print("TESS dataset info is ready.")
