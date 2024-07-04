import os
import requests
import zipfile
from tqdm import tqdm
import argparse

# funkcja pobierająca plik
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open(save_path, 'wb') as file, tqdm(
        desc=save_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=block_size,
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))

# funkcja rozpakowująca zip
def extract_zip(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Argumenty wiersza poleceń
parser = argparse.ArgumentParser(description='Pobieranie i rozpakowywanie danych.')
parser.add_argument('--ravdess_path', default=r'../download_data/RAVDESS', help='Ścieżka do katalogu RAVDESS')
parser.add_argument('--nemo_path', default=r'../download_data/nEMO', help='Ścieżka do katalogu nEMO')
parser.add_argument('--zip_path', default=r'../download_data/zip', help='Ścieżka do katalogu ZIP')

args = parser.parse_args()

# ŚCIEŻKI
ravdess_path = args.ravdess_path
nemo_path = args.nemo_path
zip_path = args.zip_path

os.makedirs(ravdess_path, exist_ok=True)
os.makedirs(nemo_path, exist_ok=True)
os.makedirs(zip_path, exist_ok=True)

# URL-e do plików ZIP
ravdess_urls = {
    'https://zenodo.org/records/1188976/files/Audio_Song_Actors_01-24.zip?download=1': 'audio_song',
    'https://zenodo.org/records/1188976/files/Audio_Speech_Actors_01-24.zip?download=1': 'audio_speech'
}

nemo_url = 'https://github.com/amu-cai/nEMO/archive/refs/heads/main.zip'

# pobieranie i rozpakowywanie plików RAVDESS
for url, folder_name in ravdess_urls.items():
    file_name = os.path.join(zip_path, url.split('/')[-1].split('?')[0])
    download_file(url, file_name)
    extract_to = os.path.join(ravdess_path, folder_name)
    os.makedirs(extract_to, exist_ok=True)
    extract_zip(file_name, extract_to)

# pobieranie i rozpakowywanie pliku nEMO
nemo_file_name = os.path.join(zip_path, nemo_url.split('/')[-1])
download_file(nemo_url, nemo_file_name)
extract_zip(nemo_file_name, nemo_path)

print("Pobieranie i rozpakowywanie zakończone.")
