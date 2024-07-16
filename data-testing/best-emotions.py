import pandas as pd

# Wczytanie pliku CSV
file_path = '/Users/maciejwylecial/Developer/praktyki-Techmo/13_07/praktyki-techmo/experiments_results/test_results_1507_RAVDESS.csv'
df = pd.read_csv(file_path)

# Filtrowanie tylko wierszy z emocjami
emotion_df = df[~df['emotion'].isin(['accuracy', 'macro avg', 'weighted avg'])]

# Grupa według nazwy eksperymentu
grouped = emotion_df.groupby('experiment_name')

# Tworzenie wynikowego słownika
results = {}

for name, group in grouped:
    # Najlepiej rozpoznawana emocja (najwyższa wartość F1-score)
    best_recognized_emotion = group.loc[group['f1-score'].idxmax()]

    # Emocje z recall powyżej 0.5
    emotions_with_high_recall = group[group['recall'] > 0.5]

    results[name] = {
        'best_recognized_emotion': best_recognized_emotion['emotion'],
        'emotions_with_high_recall': emotions_with_high_recall['emotion'].tolist()
    }

# Wyświetlenie wyników
for experiment, data in results.items():
    print(f"Experiment: {experiment}")
    print(f"Best Recognized Emotion: {data['best_recognized_emotion']}")
    print("Emotions with Recall > 0.5: ", ", ".join(data['emotions_with_high_recall']))
    print("\n")
