import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from tqdm import tqdm
import joblib

# nazwa folderu
default_experiment_name = 'knn_lda_connected'

# dodawanie z wiersza polecen
if len(sys.argv) > 1:
    experiment_name = sys.argv[1]
else:
    experiment_name = default_experiment_name

# jak nie istnieje to tworzenie katalogu
os.makedirs(experiment_name, exist_ok=True)

tqdm.pandas()  

# sciezki do danych
train_data_paths = [
    r'../four-emotions-csv-sets/train_four_emotions_RAVDESS_features.csv',
    r'../four-emotions-csv-sets/train_four_emotions_nEMO_features.csv'
]
test_data_paths = [
    r'../four-emotions-csv-sets/test_four_emotions_RAVDESS_features.csv',
    r'../four-emotions-csv-sets/test_four_emotions_nEMO_features.csv'
]

# ladowanie i laczenie zbiorow danych w przypadku wiecej niz jednego train i twst 
def load_and_combine_data(paths):
    data_frames = [pd.read_csv(path) for path in paths if os.path.exists(path)]
    if len(data_frames) > 1:
        print("Łączenie zbiorów danych")
        return pd.concat(data_frames, axis=0)
    elif data_frames:
        print("Załadowano pojedynczy zbiór danych")
        return data_frames[0]
    else:
        raise FileNotFoundError("Nie znaleziono plików danych w podanych ścieżkach.")

# wykorzystanie powyzszej funkcji
print("Ładowanie danych treningowych...")
train_data = load_and_combine_data(train_data_paths)
print("Ładowanie danych testowych...")
test_data = load_and_combine_data(test_data_paths)

# funkcja do konwersji list w kolumnach do rzeczywistych list
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in tqdm(columns_to_convert, desc="Konwertowanie kolumn"):
        data[col] = data[col].progress_apply(lambda x: np.array(eval(x.strip())))
    return data

# wykorzystanie tej fukcji
print("Konwertowanie kolumn dla danych treningowych...")
train_data = convert_columns(train_data)
print("Konwertowanie kolumn dla danych testowych...")
test_data = convert_columns(test_data)

# usuwanie białych znaków z kolumn kategorycznych
print("Usuwanie białych znaków z kolumn kategorycznych...")
train_data['emotion'] = train_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()

# kodowanie zmiennej docelowej (etykiety)
print("Kodowanie zmiennej docelowej...")
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])

# przygotowanie danych treningowych
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
print("Przygotowanie cech dla danych treningowych...")
X_train = np.concatenate([np.vstack(train_data[col].values) for col in tqdm(columns_to_convert, desc="Przygotowywanie X_train")], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# przygotowanie danych testowych
print("Przygotowanie cech dla danych testowych...")
X_test = np.concatenate([np.vstack(test_data[col].values) for col in tqdm(columns_to_convert, desc="Przygotowywanie X_test")], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# ""normalizacja cech""
print("Normalizacja cech...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# LDA preprocessing
print("Przetwarzanie LDA...")
lda = LinearDiscriminantAnalysis(n_components=3)
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# definiowanie modelu kNN i parametrów do grid search
knn = KNeighborsClassifier()
param_grid = {
    'n_neighbors': np.arange(1, 31),
    'metric': ['euclidean', 'manhattan', 'minkowski', 'chebyshev', 'hamming', 'canberra', 'braycurtis', 'cosine', 'correlation']
}

# grid search z F1-score
print("Przeprowadzanie grid search...")
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='f1_macro', verbose=3)
grid_search.fit(X_train_lda, y_train)

# wyświetlenie i zapisanie najlepszych parametrów i najlepszego wyniku
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best parameters found: ", best_params)
print("Best cross-validation F1-score: ", best_score)

# zapisanie wyników do scores.txt 
scores_path = os.path.join(experiment_name, 'scores.txt')
with open(scores_path, 'w') as f:
    f.write(f"Best parameters found: {best_params}\n")
    f.write(f"Best cross-validation F1-score: {best_score}\n")

# testowanie modelu na zestawie testowym
print("Testowanie modelu na zestawie testowym...")
best_knn = grid_search.best_estimator_
y_pred = best_knn.predict(X_test_lda)
test_accuracy = accuracy_score(y_test, y_pred)
test_f1_score = f1_score(y_test, y_pred, average='macro')

print("Test set accuracy: ", test_accuracy)
print("Test set F1-score: ", test_f1_score)

# zapisanie wszystkich niezbędnych komponentów w tym zdefiniowanym folderu
joblib.dump(label_encoder, os.path.join(experiment_name, 'label_encoder.pkl'))
joblib.dump(scaler, os.path.join(experiment_name, 'scaler.pkl'))
joblib.dump(best_knn, os.path.join(experiment_name, 'knn_model.pkl'))
joblib.dump(lda, os.path.join(experiment_name, 'lda.pkl'))
