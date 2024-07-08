import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Załadowanie danych z plików CSV
train_data = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\train_four_emotions_nEMO_features.csv')
test_data = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\test_four_emotions_nEMO_features.csv')

# Funkcja do konwersji list w kolumnach do rzeczywistych list
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in columns_to_convert:
        data[col] = data[col].apply(lambda x: np.array(eval(x.strip())))
    return data

# Konwersja list w kolumnach dla zbiorów treningowych i testowych
train_data = convert_columns(train_data)
test_data = convert_columns(test_data)

# Usuwanie białych znaków z kolumn kategorycznych
train_data['emotion'] = train_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()

# Kodowanie zmiennej docelowej (etykiety)
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])

# Przygotowanie cech (X) i etykiet (y) dla danych treningowych
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
X_train = np.concatenate([np.vstack(train_data[col].values) for col in columns_to_convert], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# Przygotowanie cech (X) i etykiet (y) dla danych testowych
X_test = np.concatenate([np.vstack(test_data[col].values) for col in columns_to_convert], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# Normalizacja cech
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definiowanie modelu kNN i parametrów do grid search
knn = KNeighborsClassifier()
param_grid = {
    'n_neighbors': np.arange(1, 31),
    'metric': ['euclidean', 'manhattan', 'minkowski', 'chebyshev', 'hamming', 'canberra', 'braycurtis', 'cosine', 'correlation']
}

# Przeprowadzenie grid search z F1-score
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='f1_macro')
grid_search.fit(X_train, y_train)

# Wyświetlenie najlepszych parametrów
print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validation F1-score: ", grid_search.best_score_)

# Testowanie modelu na zestawie testowym
best_knn = grid_search.best_estimator_
y_pred = best_knn.predict(X_test)
print("Test set accuracy: ", accuracy_score(y_test, y_pred))
print("Test set F1-score: ", f1_score(y_test, y_pred, average='macro'))
