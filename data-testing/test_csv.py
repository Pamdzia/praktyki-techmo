import pandas as pd

# ścieżka do pliku
csv_path = '../experiments_results/test_results_1507_RAVDESS.csv'

# Wczytanie pliku CSV
df = pd.read_csv(csv_path)

# filtracja tylko interesujących nas emocji i accuracy
emotions = ['angry', 'happy', 'neutral', 'sad']
filtered_df = df[df['emotion'].isin(emotions)]

# grupowanie po nazwie eksperymentu i emocjach, oraz obliczanie średniej accuracy
result_df = filtered_df.groupby(['experiment_name', 'emotion']).agg({'recall': 'mean'}).reset_index()

# format tabeli jaki chcemy
pivot_df = result_df.pivot(index='experiment_name', columns='emotion', values='recall').reset_index()

# brakujące wartości zerami
pivot_df = pivot_df.fillna(0)

print(pivot_df)

# wyniki do csv
output_csv_path = 'RAVDESS_1507.csv'
pivot_df.to_csv(output_csv_path, index=False)
