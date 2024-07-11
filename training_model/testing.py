import numpy as np
import pandas as pd
import os
import sys
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Pobieranie nazwy eksperymentu z argumentów wiersza poleceń lub użycie domyślnej
if len(sys.argv) > 1:
    experiment_name = sys.argv[1]
else:
    experiment_name = 'mlp_RAVDESS'  # Domyślna nazwa eksperymentu

results_folder = '../experiments_results'  # Ścieżka do folderu wynikowego

# Ładowanie skalera, kodera etykiet oraz modelu PCA (jeśli istnieje)
scaler = joblib.load(os.path.join(experiment_name, 'scaler.pkl'))
label_encoder = joblib.load(os.path.join(experiment_name, 'label_encoder.pkl'))
use_lda = 'lda' in experiment_name.lower()
use_rf = 'forest' in experiment_name.lower()
use_pca = 'pca' in experiment_name.lower()
use_svc = 'svc' in experiment_name.lower()
use_mlp = 'mlp' in experiment_name.lower()

if use_rf:
    model = joblib.load(os.path.join(experiment_name, 'random_forest_model.pkl'))
elif use_lda:
    lda = joblib.load(os.path.join(experiment_name, 'lda.pkl'))
    model = joblib.load(os.path.join(experiment_name, 'knn_model.pkl'))
elif use_svc:
    model = joblib.load(os.path.join(experiment_name, 'svc_model.pkl'))
elif use_mlp:
    model = joblib.load(os.path.join(experiment_name, 'mlp_model.pkl'))
else:
    model = joblib.load(os.path.join(experiment_name, 'knn_model.pkl'))

if use_pca:
    pca = joblib.load(os.path.join(experiment_name, 'pca.pkl'))

def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in columns_to_convert:
        data[col] = data[col].apply(lambda x: np.array(eval(x.strip())))
    return data

def load_and_prepare_data(file_path):
    data = pd.read_csv(file_path)
    data = convert_columns(data)
    data['emotion'] = data['emotion'].str.strip()
    data['emotion'] = label_encoder.transform(data['emotion'])
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    X = np.concatenate([np.vstack(data[col].values) for col in columns_to_convert], axis=1)
    X = np.hstack([X, data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
    X = scaler.transform(X)
    return X, data['emotion']

X_test, y_test = load_and_prepare_data('../four-emotions-csv-sets/test_four_emotions_RAVDESS_features.csv')
if use_lda:
    X_test = lda.transform(X_test)
if use_pca:
    X_test = pca.transform(X_test)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Dokładność ogólna: ", accuracy)

# Obliczanie dokładności dla każdej emocji
cm = confusion_matrix(y_test, y_pred)
class_accuracy = cm.diagonal() / cm.sum(axis=1)

# Generowanie raportu klasyfikacji
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_, zero_division=1, output_dict=True)
for i, emotion in enumerate(label_encoder.classes_):
    report[emotion]['accuracy'] = class_accuracy[i]

print("Szczegółowy raport klasyfikacji:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_, zero_division=1))

# Zapisywanie wyników do wspólnej CSV
csv_path = os.path.join(results_folder, 'test_results_1207_RAVDESS.csv')
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
report_df = pd.DataFrame(report).transpose()
report_df.reset_index(inplace=True)
report_df.rename(columns={'index': 'emotion'}, inplace=True)
report_df['experiment_name'] = experiment_name
report_df.to_csv(csv_path, mode='a', header=not os.path.isfile(csv_path), index=False)
print("Wyniki zapisane do pliku CSV:", csv_path)
