import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from tqdm import tqdm
import joblib
from matplotlib import pyplot as plt
from keras import models, layers
from tensorflow.compat.v1 import ConfigProto, InteractiveSession
from keras.utils import to_categorical

# Zdefiniowanie nazwy folderu
default_experiment_name = 'MLP_from_git_RAVDESS'

# Z linii komend nazwa
if len(sys.argv) > 1:
    experiment_name = sys.argv[1]
else:
    experiment_name = default_experiment_name

# Stworzenie folderu jak nie istnieje
os.makedirs(experiment_name, exist_ok=True)

tqdm.pandas()

# Ścieżki do plików
train_data_paths = [
    r'../four-emotions-csv-sets/train_four_emotions_RAVDESS_features.csv'
]
dev_data_paths = [
    r'../four-emotions-csv-sets/dev_four_emotions_RAVDESS_features.csv'
]
test_data_paths = [
    r'../four-emotions-csv-sets/test_four_emotions_RAVDESS_features.csv'
]

# Funkcje do załadowania i łączenia datasetów train, dev i test
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

# Wykorzystanie tej funkcji powyżej
print("Loading training data...")
train_data = load_and_combine_data(train_data_paths)
print("Loading dev data...")
dev_data = load_and_combine_data(dev_data_paths)
print("Loading test data...")
test_data = load_and_combine_data(test_data_paths)

# Konwersja list w kolumnach do aktualnych list
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in tqdm(columns_to_convert, desc="Converting columns"):
        data[col] = data[col].progress_apply(lambda x: np.array(eval(x.strip())))
    return data

# Wykorzystanie tej funkcji powyżej
print("Converting columns for training data...")
train_data = convert_columns(train_data)
print("Converting columns for dev data...")
dev_data = convert_columns(dev_data)
print("Converting columns for test data...")
test_data = convert_columns(test_data)

# Usunięcie białych przestrzeni
print("Removing whitespace from categorical columns...")
train_data['emotion'] = train_data['emotion'].str.strip()
dev_data['emotion'] = dev_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()

# 0-3 labelki
print("Encoding target variable...")
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
dev_data['emotion'] = label_encoder.transform(dev_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])

# Przygotowanie train data
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
print("Preparing features for training data...")
X_train = np.concatenate([np.vstack(train_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_train")], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# Przygotowanie dev data
print("Preparing features for dev data...")
X_dev = np.concatenate([np.vstack(dev_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_dev")], axis=1)
X_dev = np.hstack([X_dev, dev_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_dev = dev_data['emotion']

# Przygotowanie test data
print("Preparing features for test data...")
X_test = np.concatenate([np.vstack(test_data[col].values) for col in tqdm(columns_to_convert, desc="Preparing X_test")], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# Skalowanie
print("Normalizing features...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_dev = scaler.transform(X_dev)
X_test = scaler.transform(X_test)

# Konwersja y_train, y_dev i y_test do wektorów one-hot
y_train = to_categorical(y_train)
y_dev = to_categorical(y_dev)
y_test = to_categorical(y_test)

# Konfiguracja TensorFlow
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# Budowanie modelu MLP
model = models.Sequential()
model.add(layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(y_train.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Trening modelu
history = model.fit(X_train, y_train, batch_size=256, epochs=1000, verbose=1, validation_data=(X_dev, y_dev))

# Funkcja do wykresu
def plotter(history):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend(loc='upper right')
    plt.show()

# Wykres historii treningu
plotter(history)

# Podsumowanie modelu
model.summary()

# Ewaluacja modelu na zbiorze testowym
print("Testing the model on the test set...")
result = model.evaluate(X_test, y_test)
test_accuracy = result[1]
test_loss = result[0]

print("Test set accuracy: ", test_accuracy)
print("Test set loss: ", test_loss)

# Zapis wyników do scores.txt
scores_path = os.path.join(experiment_name, 'scores.txt')
with open(scores_path, 'w') as f:
    f.write(f"Test set accuracy: {test_accuracy}\n")
    f.write(f"Test set loss: {test_loss}\n")

# Zapis modelu
model.save(os.path.join(experiment_name, 'mlp_model.h5'))
joblib.dump(label_encoder, os.path.join(experiment_name, 'label_encoder.pkl'))
joblib.dump(scaler, os.path.join(experiment_name, 'scaler.pkl'))
