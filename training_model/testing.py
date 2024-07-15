import numpy as np
import pandas as pd
import os
import sys
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Pobieranie nazwy zbioru danych i eksperymentu z argumentów wiersza poleceń lub użycie domyślnych
if len(sys.argv) > 2:
    dataset_name = sys.argv[1]
    experiment_name = sys.argv[2]
elif len(sys.argv) > 1:
    dataset_name = sys.argv[1]
    experiment_name = 'mlp_' + dataset_name  # Domyślna nazwa eksperymentu
else:
    dataset_name = 'RAVDESS'  # Domyślna nazwa zbioru danych
    experiment_name = 'mlp_' + dataset_name  # Domyślna nazwa eksperymentu

experiment = '1307'  # Nazwa eksperymentu do zapisu plików, przykładowo aktualna data
results_folder = '../experiments_results'  # Ścieżka do folderu wynikowego
experiment_folder = os.path.join(results_folder, experiment)  # Ścieżka do folderu konkretnego eksperymentu

# Pobieranie dodatkowych ścieżek z argumentów wiersza poleceń
if len(sys.argv) > 3:
    test_file_path = sys.argv[3]
else:
    test_file_path = f'../four-emotions-csv-sets/test_four_emotions_{dataset_name}_features.csv'

# Ładowanie skalera, kodera etykiet oraz modelu PCA (jeśli istnieje)
try:
    scaler = joblib.load(os.path.join(experiment_name, 'scaler.pkl'))
    label_encoder = joblib.load(os.path.join(experiment_name, 'label_encoder.pkl'))
except FileNotFoundError as e:
    print(f"Błąd: {e}")
    sys.exit(1)

use_lda = 'lda' in experiment_name.lower()
use_rf = 'forest' in experiment_name.lower()
use_pca = 'pca' in experiment_name.lower()
use_svc = 'svc' in experiment_name.lower()
use_mlp = 'mlp' in experiment_name.lower()

try:
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
except FileNotFoundError as e:
    print(f"Błąd: {e}")
    sys.exit(1)

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

# Załadowanie danych testowych
try:
    X_test, y_test = load_and_prepare_data(test_file_path)
except FileNotFoundError as e:
    print(f"Błąd: {e}")
    sys.exit(1)

if use_lda:
    X_test = lda.transform(X_test)
if use_pca:
    X_test = pca.transform(X_test)
y_pred = model.predict(X_test)

# Obliczanie ogólnej dokładności
overall_accuracy = accuracy_score(y_test, y_pred)
print("Dokładność ogólna: ", overall_accuracy)

# Obliczanie macierzy pomyłek
cm = confusion_matrix(y_test, y_pred)

# Inicjalizacja list na metryki
class_accuracies = []
class_recalls = []
class_precisions = []
class_f1s = []
supports = []

# Obliczanie metryk dla każdej klasy
for i, emotion in enumerate(label_encoder.classes_):
    TP = cm[i, i]
    FN = cm[i, :].sum() - TP
    FP = cm[:, i].sum() - TP
    TN = cm.sum() - (TP + FN + FP)
    
    class_accuracy = (TP + TN) / (TP + TN + FP + FN)
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    class_accuracies.append(class_accuracy)
    class_recalls.append(recall)
    class_precisions.append(precision)
    class_f1s.append(f1)
    supports.append(cm[i, :].sum())

# Generowanie raportu klasyfikacji
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_, zero_division=1, output_dict=True)
for i, emotion in enumerate(label_encoder.classes_):
    report[emotion]['class_accuracy'] = class_accuracies[i]
    report[emotion]['recall'] = class_recalls[i]
    report[emotion]['precision'] = class_precisions[i]
    report[emotion]['f1-score'] = class_f1s[i]
    report[emotion]['support'] = supports[i]

print("Szczegółowy raport klasyfikacji:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_, zero_division=1))

# Dodanie ogólnej dokładności do raportu
report['accuracy'] = {
    'precision': overall_accuracy,
    'recall': overall_accuracy,
    'f1-score': overall_accuracy,
    'support': len(y_test),
    'class_accuracy': overall_accuracy
}

# Tworzenie folderu na wyniki eksperymentu
if not os.path.exists(experiment_folder):
    os.makedirs(experiment_folder)

# Zapisywanie macierzy pomyłek do pliku
cm_filename = f'{experiment_name}_{dataset_name}_confusion_matrix.csv'
cm_path = os.path.join(experiment_folder, cm_filename)
cm_df = pd.DataFrame(cm, index=label_encoder.classes_, columns=label_encoder.classes_)
cm_df.to_csv(cm_path)
print("Macierz pomyłek zapisana do pliku:", cm_path)

# Normalizacja macierzy pomyłek dla wizualizacji
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

# Zapisywanie macierzy pomyłek jako obrazek PNG
plt.figure(figsize=(10, 8))
sns.heatmap(cm_normalized, annot=True, fmt=".2f", cmap="Blues", xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Przewidywane etykiety')
plt.ylabel('Rzeczywiste etykiety')
plt.title('Znormalizowana macierz pomyłek')
plt.savefig(os.path.join(experiment_folder, f'{experiment_name}_{dataset_name}_confusion_matrix.png'))
plt.close()

# Zapisywanie raportu klasyfikacji do pliku w folderze eksperymentu
report_filename = f'{experiment_name}_{dataset_name}_classification_report.csv'
report_path = os.path.join(experiment_folder, report_filename)
report_df = pd.DataFrame(report).transpose()
report_df.reset_index(inplace=True)
report_df.rename(columns={'index': 'emotion'}, inplace=True)
report_df.to_csv(report_path, index=False)
print("Raport klasyfikacji zapisany do pliku:", report_path)

# Wyciąganie wartości weighted f1-score
weighted_f1_score = report['weighted avg']['f1-score']

# Zapisywanie weighted f1-score do pliku CSV w folderze eksperymentu
f1_score_path = os.path.join(experiment_folder, 'f1_scores.csv')
# Dodanie nazwy zbioru danych jako kolumny w DataFrame
f1_score_df = pd.DataFrame({
    'f1-score': [weighted_f1_score],
    'experiment_name': [experiment_name],
    'dataset_name': [dataset_name]  # Dodanie nazwy datasetu
})
f1_score_df.to_csv(f1_score_path, mode='a', header=not os.path.isfile(f1_score_path), index=False)
print("Wartość weighted f1-score zapisana do pliku:", f1_score_path)

# Zapisywanie pełnego raportu do wspólnej CSV w katalogu wyników
csv_path = os.path.join(results_folder, f'test_results_{experiment}_{dataset_name}.csv')
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
report_df['experiment_name'] = experiment_name
report_df.to_csv(csv_path, mode='a', header=not os.path.isfile(csv_path), index=False)
print("Wyniki zapisane do pliku CSV:", csv_path)
