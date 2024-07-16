import pandas as pd

# Wczytanie pliku CSV
file_path = '../experiments_results/test_results_1507_RAVDESS.csv'
df = pd.read_csv(file_path)

# Filtrowanie tylko wierszy z emocjami
emotion_df = df[~df['emotion'].isin(['accuracy', 'macro avg', 'weighted avg'])]

# Grupa według nazwy eksperymentu
grouped = emotion_df.groupby('experiment_name')

# Funkcja do generowania wyników
def generate_results(metric):
    results = {}
    for name, group in grouped:
        # Najlepiej rozpoznawana emocja (najwyższa wartość wybranego metryki)
        best_recognized_emotion = group.loc[group[metric].idxmax()]
        best_emotion = best_recognized_emotion['emotion']
        best_metric_value = round(best_recognized_emotion[metric], 2)

        # Emocje z metryką powyżej 0.5
        emotions_with_high_metric = group[group[metric] > 0.5]

        # Emocje z metryką poniżej 0.2
        emotions_with_low_metric = group[group[metric] < 0.2]

        results[name] = {
            'best_recognized_emotion': (best_emotion, best_metric_value),
            'emotions_with_high_metric': emotions_with_high_metric['emotion'].tolist(),
            'emotions_with_low_metric': [(row['emotion'], round(row[metric], 2)) for idx, row in emotions_with_low_metric.iterrows()]
        }
    return results

# Funkcja do zapisu wyników do pliku tekstowego
def save_results_to_file(results, metric, filename):
    with open(filename, 'w') as file:
        for experiment, data in results.items():
            best_emotion, best_metric_value = data['best_recognized_emotion']
            file.write(f"Experiment: {experiment}\n")
            file.write(f"Best Recognized Emotion: {best_emotion} ({metric.capitalize()}: {best_metric_value})\n")
            file.write(f"Emotions with {metric.capitalize()} > 0.5: {', '.join(data['emotions_with_high_metric'])}\n")
            if data['emotions_with_low_metric']:
                low_metric_emotions = ", ".join([f"{emotion} ({metric.capitalize()}: {metric_value})" for emotion, metric_value in data['emotions_with_low_metric']])
                file.write(f"Emotions with {metric.capitalize()} < 0.2: {low_metric_emotions}\n")
            else:
                file.write(f"Emotions with {metric.capitalize()} < 0.2: None\n")
            file.write("\n")

# Generowanie wyników dla każdej metryki
metrics = ['precision', 'recall', 'f1-score']
for metric in metrics:
    results = generate_results(metric)
    filename = f"{metric}_results.txt"
    save_results_to_file(results, metric, filename)

print("Wyniki zapisane do plików tekstowych.")
