import numpy as np
import os
import joblib
from keras.models import load_model
import argparse
import librosa
import scipy.signal

def extract_features(file_path, frame_length, hop_length):
    y, sr = librosa.load(file_path, sr=None)
    hamming_window = scipy.signal.get_window("hamming", frame_length, fftbins=True)
    
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12, window=hamming_window, hop_length=hop_length, n_fft=frame_length)
    mfccs_stats = np.concatenate([np.mean(mfccs, axis=1), np.var(mfccs, axis=1), np.max(mfccs, axis=1), np.min(mfccs, axis=1), np.ptp(mfccs, axis=1)])

    pitches, _ = librosa.piptrack(y=y, sr=sr, window=hamming_window, hop_length=hop_length, n_fft=frame_length)
    pitches = pitches[pitches > 0]
    pitch_stats = np.array([np.mean(pitches), np.var(pitches), np.max(pitches), np.min(pitches), np.ptp(pitches)]) if len(pitches) > 0 else np.zeros(5)

    energy = np.array([np.sum(np.abs(y[i:i+frame_length]**2)) for i in range(0, len(y), hop_length)])
    energy_stats = np.array([np.mean(energy), np.var(energy), np.max(energy), np.min(energy), np.ptp(energy)])

    zero_crossing_rate = librosa.feature.zero_crossing_rate(y, frame_length=frame_length, hop_length=hop_length)
    zcr_stats = np.array([np.mean(zero_crossing_rate), np.var(zero_crossing_rate), np.max(zero_crossing_rate), np.min(zero_crossing_rate), np.ptp(zero_crossing_rate)])
    
    return np.concatenate([mfccs_stats, pitch_stats, energy_stats, zcr_stats])

parser = argparse.ArgumentParser(description='Predykcja emocji z pliku audio.')
parser.add_argument('--model_dir', required=True, help='Ścieżka do katalogu z modelem')
parser.add_argument('--audio_path', required=True, help='Ścieżka do pliku audio')

args = parser.parse_args()

model_dir = args.model_dir
audio_path = args.audio_path

scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
label_encoder = joblib.load(os.path.join(model_dir, 'label_encoder.pkl'))

use_rf = 'forest' in model_dir.lower()
use_lda = 'lda' in model_dir.lower()
use_svc = 'svc' in model_dir.lower()
use_mlp_sklearn = 'mlp' in model_dir.lower() and 'from_git' not in model_dir.lower()
use_mlp_keras = 'mlp_from_git' in model_dir.lower()

try:
    if use_rf:
        model = joblib.load(os.path.join(model_dir, 'random_forest_model.pkl'))
    elif use_lda:
        lda = joblib.load(os.path.join(model_dir, 'lda.pkl'))
        model_file = 'svc_model.pkl' if use_svc else 'knn_model.pkl'
        model = joblib.load(os.path.join(model_dir, model_file))
    elif use_svc:
        model = joblib.load(os.path.join(model_dir, 'svc_model.pkl'))
    elif use_mlp_sklearn:
        model = joblib.load(os.path.join(model_dir, 'mlp_model.pkl'))
    elif use_mlp_keras:
        model = load_model(os.path.join(model_dir, 'mlp_model.keras'))
    else:
        model = joblib.load(os.path.join(model_dir, 'knn_model.pkl'))
except FileNotFoundError as e:
    print(f"Błąd: {e}")
    sys.exit(1)

frame_length = 2048
hop_length = 512

features = extract_features(audio_path, frame_length, hop_length)
features = features.reshape(1, -1)

features_scaled = scaler.transform(features)

if use_mlp_keras:
    predictions = model.predict(features_scaled)
    predicted_label = np.argmax(predictions, axis=1)[0]
else:
    predicted_label = model.predict(features_scaled)[0]

predicted_emotion = label_encoder.inverse_transform([predicted_label])[0]
print(f"Predykowana emocja: {predicted_emotion}")
