import pandas as pd

# Wczytanie pliku CSV
file_path = '../experiments_results/test_results_1507_nEMO.csv'
df = pd.read_csv(file_path)

# Filtrowanie tylko wierszy z emocjami
emotion_df = df[~df['emotion'].isin(['accuracy', 'macro avg', 'weighted avg'])]

# Grupa według nazwy eksperymentu
grouped = emotion_df.groupby('experiment_name')

# Tworzenie wynikowego słownika
results = {}

for name, group in grouped:
    # Najlepiej rozpoznawana emocja (najwyższa wartość recall)
    best_recognized_emotion = group.loc[group['recall'].idxmax()]
    best_emotion = best_recognized_emotion['emotion']
    best_recall = round(best_recognized_emotion['recall'], 2)

    # Emocje z recall powyżej 0.5
    emotions_with_high_recall = group[group['recall'] > 0.5]

    # Emocje z recall poniżej 0.2
    emotions_with_low_recall = group[group['recall'] < 0.2]

    results[name] = {
        'best_recognized_emotion': (best_emotion, best_recall),
        'emotions_with_high_recall': emotions_with_high_recall['emotion'].tolist(),
        'emotions_with_low_recall': [(row['emotion'], round(row['recall'], 2)) for idx, row in emotions_with_low_recall.iterrows()]
    }

# Wyświetlenie wyników
for experiment, data in results.items():
    best_emotion, best_recall = data['best_recognized_emotion']
    print(f"Experiment: {experiment}")
    print(f"Best Recognized Emotion: {best_emotion} (Recall: {best_recall})")
    print("Emotions with Recall > 0.5: ", ", ".join(data['emotions_with_high_recall']))
    if data['emotions_with_low_recall']:
        low_recall_emotions = ", ".join([f"{emotion} (Recall: {recall})" for emotion, recall in data['emotions_with_low_recall']])
        print(f"Emotions with Recall < 0.2: {low_recall_emotions}")
    else:
        print("Emotions with Recall < 0.2: None")
    print("\n")
