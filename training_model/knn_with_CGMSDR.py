import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from tqdm import tqdm
import joblib

# nazwa folderu gdzie zapisywany model z danymi
default_experiment_name = 'knn_with_CGMSDR_connected'

# nazwanie folderu z lini polecen
if len(sys.argv) > 1:
    experiment_name = sys.argv[1]
else:
    experiment_name = default_experiment_name

# stworzenie folderu jak nie istnieje
os.makedirs(experiment_name, exist_ok=True)

tqdm.pandas()  

# sciezki do plikow
train_data_paths = [
    r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\train_four_emotions_nEMO_features.csv',
    r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\train_four_emotions_RAVDESS_features.csv'
]
test_data_paths = [
    r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\clean\praktyki-techmo\four-emotions-csv-sets\test_four_emotions_RAVDESS_features.csv'
]

# funkcja do laczenia datasetow jak podane wiecej niz jeden
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

# wywolanie tej funkcji laczenia
print("Loading training data...")
train_data = load_and_combine_data(train_data_paths)
print("Loading test data...")
test_data = load_and_combine_data(test_data_paths)

# funkcja przystosowujaca zbior danych (tworzenie list)
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in tqdm(columns_to_convert, desc="Converting columns"):
        data[col] = data[col].progress_apply(lambda x: np.array(eval(x.strip())))
    return data

# konwertowanie list w kolumnach powyzsza funkcja
print("Converting columns for training data...")
train_data = convert_columns(train_data)
print("Converting columns for test data...")
test_data = convert_columns(test_data)

# usuniecie bialych przestrrzeni
print("Removing whitespace from categorical columns...")
train_data['emotion'] = train_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()

# enkodowanie target zmiennej (0-3)
print("Encoding target variable...")
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])

# przygotowanie cech i labelek do treningu
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
print("Preparing features for training data...")
X_train = np.concatenate([np.vstack(train_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_train")], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# przygotowanie cech i labelek do testu
print("Preparing features for test data...")
X_test = np.concatenate([np.vstack(test_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_test")], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# standaryzacja cech przed CGMSDR
print("Standardizing features before CGMSDR...")
standard_scaler = StandardScaler()
X_train = standard_scaler.fit_transform(X_train)
X_test = standard_scaler.transform(X_test)

# implementacja CGMSDR 
def cgmsdr(data, target, num_features):
    # obliczanie korelacji
    correlations = np.corrcoef(data, rowvar=False)
    correlation_with_target = np.abs(np.corrcoef(data.T, target)[-1][:-1])
    
    # wybór cech o wysokiej korelacji
    selected_features_indices = np.argsort(correlation_with_target)[-num_features:]
    selected_data = data[:, selected_features_indices]
    
    # redukcja wymiarowości
    pca = PCA(n_components=num_features)
    reduced_data = pca.fit_transform(selected_data)
    
    return reduced_data

# sprawdzenie optymalnej liczby cech
def find_best_num_features(X_train, y_train):
    best_num_features = 0
    best_score = 0
    best_knn_model = None
    skf = StratifiedKFold(n_splits=5)
    
    for num_features in range(1, X_train.shape[1] + 1):
        print(f"Evaluating CGMSDR with {num_features} features...")
        X_train_reduced = cgmsdr(X_train, y_train, num_features)
        
        knn = KNeighborsClassifier()
        param_grid = {
            'n_neighbors': np.arange(1, 31),
            'metric': ['euclidean', 'manhattan', 'minkowski', 'chebyshev', 'hamming', 'canberra', 'braycurtis', 'cosine', 'correlation']
        }
        
        grid_search = GridSearchCV(knn, param_grid, cv=skf, scoring='f1_macro', verbose=0)
        grid_search.fit(X_train_reduced, y_train)
        
        if grid_search.best_score_ > best_score:
            best_score = grid_search.best_score_
            best_num_features = num_features
            best_knn_model = grid_search.best_estimator_
    
    return best_num_features, best_knn_model, best_score

print("Finding the best number of features...")
best_num_features, best_knn_model, best_score = find_best_num_features(X_train, y_train)

print(f"Best number of features: {best_num_features}")
print(f"Best cross-validation F1-score: {best_score}")

# CGMSDR z najlepsza liczba cech
X_train_reduced = cgmsdr(X_train, y_train, best_num_features)
X_test_reduced = cgmsdr(X_test, y_test, best_num_features)

# normalizacja cech przed kNN
#print("Normalizing features before kNN...")
#normalizer = MinMaxScaler()
#X_train_reduced = normalizer.fit_transform(X_train_reduced)
#X_test_reduced = normalizer.transform(X_test_reduced)

# testowanie najelpszego modelu na testowych danych
print("Testing the best model on the test set...")
y_pred = best_knn_model.predict(X_test_reduced)
test_accuracy = accuracy_score(y_test, y_pred)
test_f1_score = f1_score(y_test, y_pred, average='macro')

print("Test set accuracy: ", test_accuracy)
print("Test set F1-score: ", test_f1_score)
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# zapisanie wynikow w scores.txt
scores_path = os.path.join(experiment_name, 'scores.txt')
with open(scores_path, 'w') as f:
    f.write(f"Best number of features: {best_num_features}\n")
    f.write(f"Best cross-validation F1-score: {best_score}\n")
    f.write(f"Test set accuracy: {test_accuracy}\n")
    f.write(f"Test set F1-score: {test_f1_score}\n")
    f.write(f"\nClassification Report:\n{classification_report(y_test, y_pred, target_names=label_encoder.classes_)}")

# zapisnaie wszystkich niezbednych plikow modelu
joblib.dump(label_encoder, os.path.join(experiment_name, 'label_encoder.pkl'))
joblib.dump(standard_scaler, os.path.join(experiment_name, 'standard_scaler.pkl'))
#joblib.dump(normalizer, os.path.join(experiment_name, 'normalizer.pkl'))
joblib.dump(best_knn_model, os.path.join(experiment_name, 'knn_model.pkl'))
