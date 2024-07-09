import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tqdm import tqdm
import joblib

# Define the default experiment name
default_experiment_name = 'random_forrest_RAVDESS'

# Parse command-line argument for experiment name
if len(sys.argv) > 1:
    experiment_name = sys.argv[1]
else:
    experiment_name = default_experiment_name

# Create the directory if it does not exist
os.makedirs(experiment_name, exist_ok=True)

tqdm.pandas()  # Prepare pandas to use tqdm for progress bars

# Load data from CSV files
train_data_paths = [
    r'../four-emotions-csv-sets/train_four_emotions_RAVDESS_features.csv'
]
test_data_paths = [
    r'../four-emotions-csv-sets/test_four_emotions_RAVDESS_features.csv',
    r'../four-emotions-csv-sets/test_four_emotions_NEMO_features.csv'
]

# Function to load and combine datasets if more than one file exists
def load_and_combine_data(paths):
    data_frames = [pd.read_csv(path) for path in paths if os.path.exists(path)]
    if len(data_frames) > 1:
        return pd.concat(data_frames, axis=0)
    elif data_frames:
        return data_frames[0]
    else:
        raise FileNotFoundError("No dataset files found in the specified paths.")

# Load and combine training and testing datasets
train_data = load_and_combine_data(train_data_paths)
test_data = load_and_combine_data(test_data_paths)

# Function to convert lists in columns to actual lists
def convert_columns(data):
    columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
    for col in columns_to_convert:
        data[col] = data[col].progress_apply(lambda x: np.array(eval(x.strip())))
    return data

# Convert lists in columns for training and testing datasets
train_data = convert_columns(train_data)
test_data = convert_columns(test_data)

# Remove whitespace from categorical columns
train_data['emotion'] = train_data['emotion'].str.strip()
test_data['emotion'] = test_data['emotion'].str.strip()

# Encode the target variable (labels)
label_encoder = LabelEncoder()
train_data['emotion'] = label_encoder.fit_transform(train_data['emotion'])
test_data['emotion'] = label_encoder.transform(test_data['emotion'])

# Prepare features (X) and labels (y) for training data
columns_to_convert = ['mfcc_mean', 'mfcc_var', 'mfcc_max', 'mfcc_min', 'mfcc_range']
X_train = np.concatenate([np.vstack(train_data[col].values) for col in columns_to_convert], axis=1)
X_train = np.hstack([X_train, train_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_train = train_data['emotion']

# Prepare features (X) and labels (y) for test data
X_test = np.concatenate([np.vstack(test_data[col].values) for col in columns_to_convert], axis=1)
X_test = np.hstack([X_test, test_data[['pitch_mean', 'pitch_var', 'pitch_max', 'pitch_min', 'pitch_range', 'energy_mean', 'energy_var', 'energy_max', 'energy_min', 'energy_range', 'zcr_mean', 'zcr_var', 'zcr_max', 'zcr_min', 'zcr_range']].values])
y_test = test_data['emotion']

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the Random Forest model and parameters for grid search
rf = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

# Perform grid search with F1-score
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='f1_macro', n_jobs=-1, verbose=3)
grid_search.fit(X_train, y_train)

# Display and save best parameters and best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best parameters found: ", best_params)
print("Best cross-validation F1-score: ", best_score)

# Save results to scores.txt in the experiment directory
scores_path = os.path.join(experiment_name, 'scores.txt')
with open(scores_path, 'w') as f:
    f.write(f"Best parameters found: {best_params}\n")
    f.write(f"Best cross-validation F1-score: {best_score}\n")

# Test the model on the test set
best_rf = grid_search.best_estimator_
y_pred = best_rf.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
test_f1_score = f1_score(y_test, y_pred, average='macro')

print("Test set accuracy: ", test_accuracy)
print("Test set F1-score: ", test_f1_score)

# Save all necessary components in the experiment directory
joblib.dump(label_encoder, os.path.join(experiment_name, 'label_encoder.pkl'))
joblib.dump(scaler, os.path.join(experiment_name, 'scaler.pkl'))
joblib.dump(best_rf, os.path.join(experiment_name, 'random_forest_model.pkl'))
