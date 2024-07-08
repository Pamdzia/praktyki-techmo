import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Załadowanie danych z plików CSV
train_data = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\train_four_emotions_RAVDESS_features.csv')
test_data = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\test_four_emotions_RAVDESS_features.csv')
test_data_2 = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\test_four_emotions_nEMO_features.csv')

# Funkcja do konwersji list w kolumnach do rzeczywistych list
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in columns_to_convert:
        data[col] = data[col].apply(lambda x: np.array(eval(x.strip())))
    return data

# Konwersja list w kolumnach dla zbiorów treningowych i testowych
train_data = convert_columns(train_data)
test_data = convert_columns(test_data)
test_data_2 = convert_columns(test_data_2)

# Usuwanie białych znaków z kolumn kategorycznych
train_data['emotion'] = train_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()
test_data_2['emotion'] = test_data_2['emotion'].str.strip()

# Kodowanie zmiennej docelowej (etykiety)
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])
test_data_2['emotion'] = label_encoder.transform(test_data_2['emotion'])

# Przygotowanie cech (X) i etykiet (y) dla danych treningowych
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
X_train = np.concatenate([np.vstack(train_data[col].values) for col in columns_to_convert], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# Przygotowanie cech (X) i etykiet (y) dla danych testowych
X_test = np.concatenate([np.vstack(test_data[col].values) for col in columns_to_convert], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# Przygotowanie cech (X) i etykiet (y) dla drugiego zbioru testowego
X_test_2 = np.concatenate([np.vstack(test_data_2[col].values) for col in columns_to_convert], axis=1)
X_test_2 = np.hstack([X_test_2, test_data_2[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test_2 = test_data_2['emotion']

# Normalizacja cech
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_test_2 = scaler.transform(X_test_2)

# Definiowanie modelu Random Forest i parametrów do grid search
rf = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [50, 100, 200, 300, 400],  # Więcej wartości
    'max_features': [None, 'sqrt', 'log2'],  # Więcej wartości
    'max_depth': [None, 10, 20, 30, 40, 50, 60, 70],  # Więcej wartości
    'min_samples_split': [2, 5, 10, 15],  # Więcej wartości
    'min_samples_leaf': [1, 2, 4, 6],  # Więcej wartości
    'bootstrap': [True, False]  # Dodanie bootstrap jako parametr
}

# Przeprowadzenie grid search z F1-score
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='f1_macro', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Wyświetlenie najlepszych parametrów
print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validation F1-score: ", grid_search.best_score_)

# Testowanie modelu na zestawie testowym
best_rf = grid_search.best_estimator_
y_pred = best_rf.predict(X_test)
print("Test set accuracy (RAVDESS): ", accuracy_score(y_test, y_pred))
print("Test set F1-score (RAVDESS): ", f1_score(y_test, y_pred, average='macro'))

# Testowanie modelu na drugim zestawie testowym
y_pred_2 = best_rf.predict(X_test_2)
print("Test set 2 accuracy (nEMO): ", accuracy_score(y_test_2, y_pred_2))
print("Test set 2 F1-score (nEMO): ", f1_score(y_test_2, y_pred_2, average='macro'))
