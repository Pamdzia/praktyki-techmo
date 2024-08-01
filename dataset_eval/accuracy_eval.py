import os
import pandas as pd
from tqdm import tqdm

# Ścieżka do folderu z plikami CSV
input_folder_path = "dataset_eval"
output_csv_path = "summary_accuracy.csv"

# Lista do przechowywania wyników
results = []

# Funkcja do obliczania dokładności
def calculate_accuracy(df, emotion):
    filtered_df = df[df['true_emotion'] == emotion]
    if len(filtered_df) == 0:
        return 0
    return sum(filtered_df['true_emotion'] == filtered_df['predicted_emotion']) / len(filtered_df)

# Iteracja przez każdy plik CSV w folderze
for filename in tqdm(os.listdir(input_folder_path)):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder_path, filename)
        
        # Wczytanie CSV
        df = pd.read_csv(file_path)
        
        # Lista unikalnych emocji
        emotions = df['true_emotion'].unique()
        
        # Obliczanie dokładności dla każdej emocji
        for emotion in emotions:
            accuracy = calculate_accuracy(df, emotion)
            results.append({
                "filename": filename,
                "emotion": emotion,
                "accuracy": accuracy
            })
        
        # Obliczanie średniej dokładności dla całej CSV
        overall_accuracy = sum(df['true_emotion'] == df['predicted_emotion']) / len(df)
        results.append({
            "filename": filename,
            "emotion": "overall",
            "accuracy": overall_accuracy
        })

# Zapisanie wyników do CSV
results_df = pd.DataFrame(results)
results_df.to_csv(output_csv_path, index=False)

print(f"Wyniki zostały zapisane do {output_csv_path}")
