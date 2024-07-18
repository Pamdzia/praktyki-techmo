import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tqdm import tqdm
import joblib

# zdefiniowanie nazwy folderu
default_experiment_name = 'SVC_emo_DB'

# z lini komend nazwa
if len(sys.argv) > 1:
    experiment_name = sys.argv[1]
else:
    experiment_name = default_experiment_name

# stworzenie folderu jak nie istnieje
os.makedirs(experiment_name, exist_ok=True)

tqdm.pandas()  

# sciezki do pliku/ow
train_data_paths = [
    r'../four-emotions-csv-sets/train_four_emotions_emo_DB_features.csv'
]
test_data_paths = [
    r'../four-emotions-csv-sets/test_four_emotions_emo_DB_features.csv'
]

# funkcje do zaladowania i laczenia datasetow train i test
def load_and_combine_data(paths):
    data_frames = [pd.read_csv(path) for path in paths if os.path.exists(path)]
    if len(data_frames) > 1:
        print("Combining datasets")
        return pd.concat(data_frames, axis=0)
    elif data_frames:
        print("Single dataset loaded")
        return data_frames[0]
    else:
        raise FileNotFoundError("No dataset files found in the specified paths.")

# wykorzystanie tej fnkcji powyzej
print("Loading training data...")
train_data = load_and_combine_data(train_data_paths)
print("Loading test data...")
test_data = load_and_combine_data(test_data_paths)

# konwersja list w kolumnach do aktualnych list
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in tqdm(columns_to_convert, desc="Converting columns"):
        data[col] = data[col].progress_apply(lambda x: np.array(eval(x.strip())))
    return data

# wykorzystanie tej fnkcji powyzej
print("Converting columns for training data...")
train_data = convert_columns(train_data)
print("Converting columns for test data...")
test_data = convert_columns(test_data)

# usuniecie bialych przesterzeni
print("Removing whitespace from categorical columns...")
train_data['emotion'] = train_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()

# 0-3 labelki
print("Encoding target variable...")
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])

# przygotowanue train data
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
print("Preparing features for training data...")
X_train = np.concatenate([np.vstack(train_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_train")], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# przygotowanue test data
print("Preparing features for test data...")
X_test = np.concatenate([np.vstack(test_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_test")], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# skalowanie cech
print("Normalizing features...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# zdefiniowanie random forest i parametrow grid search
svc = SVC()
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100, 1000],
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
    'kernel': ['poly', 'rbf', 'sigmoid']
}

# grid search z F1 (odpalenie grid search)
print("Performing grid search...")
grid_search = GridSearchCV(svc, param_grid, cv=5, scoring='f1_macro', verbose=3)
grid_search.fit(X_train, y_train)

# wyswietlenie i zapisanie najlepszych parametrow
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best parameters found: ", best_params)
print("Best cross-validation F1-score: ", best_score)

# zapisanie do scores.txt wynikow
scores_path = os.path.join(experiment_name, 'scores.txt')
with open(scores_path, 'w') as f:
    f.write(f"Best parameters found: {best_params}\n")
    f.write(f"Best cross-validation F1-score: {best_score}\n")

# test modelu na test set
print("Testing the model on the test set...")
best_svc = grid_search.best_estimator_
y_pred = best_svc.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
test_f1_score = f1_score(y_test, y_pred, average='macro')

print("Test set accuracy: ", test_accuracy)
print("Test set F1-score: ", test_f1_score)

# zapisnaie modelu
joblib.dump(label_encoder, os.path.join(experiment_name, 'label_encoder.pkl'))
joblib.dump(scaler, os.path.join(experiment_name, 'scaler.pkl'))
joblib.dump(best_svc, os.path.join(experiment_name, 'svc_model.pkl'))
