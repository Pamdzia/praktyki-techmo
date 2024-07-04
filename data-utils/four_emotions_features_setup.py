import os
import pandas as pd
import numpy as np
import librosa
import scipy.signal
from tqdm import tqdm

# SCIEZKII
base_path = r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\downloaded_data\RAVDESS'
csv_path = r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data-utils\four_emotions_RAVDESS.csv'
output_dir = r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\four_emotions_csvs_all'

BASE_PATH = os.getenv('BASE_PATH', base_path)
CSV_PATH = os.getenv('CSV_PATH', csv_path)
OUTPUT_DIR = os.getenv('OUTPUT_DIR', output_dir)

# sciekza do pliku wyjsciowego
csv_filename = os.path.basename(CSV_PATH)
output_filename = csv_filename.replace('.csv', '_features.csv')
OUTPUT_PATH = os.path.join(OUTPUT_DIR, output_filename)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# ILE WSPOLCZYNNIKOW MFCC
n_mfcc = 12

def extract_features(file_path, frame_length, hop_length):
    y, sr = librosa.load(file_path, sr=None)
    hamming_window = scipy.signal.get_window("hamming", frame_length, fftbins=True)
    
    # MFCC
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, window=hamming_window, hop_length=hop_length, n_fft=frame_length)
    mfccs_stats = {
        'mfcc_mean': np.mean(mfccs, axis=1).tolist(),
        'mfcc_var': np.var(mfccs, axis=1).tolist(),
        'mfcc_max': np.max(mfccs, axis=1).tolist(),
        'mfcc_min': np.min(mfccs, axis=1).tolist(),
        'mfcc_range': (np.max(mfccs, axis=1) - np.min(mfccs, axis=1)).tolist()
    }

    # pitch z autocorrelation
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr, window=hamming_window, hop_length=hop_length, n_fft=frame_length)
    pitches = pitches[pitches > 0]
    if len(pitches) > 0:
        pitch_stats = {
            'pitch_mean': np.mean(pitches).tolist(),
            'pitch_var': np.var(pitches).tolist(),
            'pitch_max': np.max(pitches).tolist(),
            'pitch_min': np.min(pitches).tolist(),
            'pitch_range': (np.max(pitches) - np.min(pitches)).tolist()
        }
    else:
        pitch_stats = {
            'pitch_mean': 0,
            'pitch_var': 0,
            'pitch_max': 0,
            'pitch_min': 0,
            'pitch_range': 0
        }

    # energia
    energy = np.array([np.sum(np.abs(y[i:i+frame_length]**2)) for i in range(0, len(y), hop_length)])
    energy_stats = {
        'energy_mean': np.mean(energy).tolist(),
        'energy_var': np.var(energy).tolist(),
        'energy_max': np.max(energy).tolist(),
        'energy_min': np.min(energy).tolist(),
        'energy_range': (np.max(energy) - np.min(energy)).tolist()
    }

    # ZCR
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y, frame_length=frame_length, hop_length=hop_length)
    zcr_stats = {
        'zcr_mean': np.mean(zero_crossing_rate).tolist(),
        'zcr_var': np.var(zero_crossing_rate).tolist(),
        'zcr_max': np.max(zero_crossing_rate).tolist(),
        'zcr_min': np.min(zero_crossing_rate).tolist(),
        'zcr_range': (np.max(zero_crossing_rate) - np.min(zero_crossing_rate)).tolist()
    }

    features = {}
    features.update(mfccs_stats)
    features.update(pitch_stats)
    features.update(energy_stats)
    features.update(zcr_stats)
    
    return features

data = pd.read_csv(CSV_PATH, sep=',')
data['full_path'] = data['relative path'].apply(lambda x: os.path.join(BASE_PATH, x.strip()))

# uzyskanie częstotliwości próbkowania - wczytanie pierwszego pliku audio
first_file_path = data['full_path'].iloc[0]
y, sr = librosa.load(first_file_path, sr=None)

# okno Hamminga o długości 20ms i przesunięciu 10ms na podstawie częstotliwości próbkowania
frame_length = int(0.02 * sr)  # 20 ms
hop_length = int(0.01 * sr)  # 10 ms

results = []
for _, row in tqdm(data.iterrows(), total=len(data), desc="Extracting features"):
    file_features = extract_features(row['full_path'], frame_length, hop_length)
    for col in data.columns:
        if col != 'full_path':  
            file_features[col] = row[col]
    results.append(file_features)

features_df = pd.DataFrame(results)

# oryginalna kolejnosc kolumn
cols = [col for col in data.columns if col != 'full_path'] + [col for col in features_df.columns if col not in data.columns]
features_df = features_df[cols]

features_df.to_csv(OUTPUT_PATH, index=False)
