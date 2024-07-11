import pandas as pd

# Ścieżka do pliku CSV
csv_path = '../experiments_results/test_results_1207_nEMO.csv'

# Wczytanie pliku CSV
df = pd.read_csv(csv_path)

# Filtracja tylko interesujących nas emocji i accuracy
emotions = ['angry', 'happy', 'neutral', 'sad']
filtered_df = df[df['emotion'].isin(emotions)]

# Grupowanie po nazwie eksperymentu i emocjach, oraz obliczanie średniej accuracy
result_df = filtered_df.groupby(['experiment_name', 'emotion']).agg({'accuracy': 'mean'}).reset_index()

# Pivotowanie tabeli, aby uzyskać pożądany format
pivot_df = result_df.pivot(index='experiment_name', columns='emotion', values='accuracy').reset_index()

# Zastąpienie brakujących wartości zerami (jeśli są takie przypadki)
pivot_df = pivot_df.fillna(0)

# Wyświetlenie wyników
print(pivot_df)

# Opcjonalnie zapisanie wyników do pliku CSV
output_csv_path = 'nEMO_1207.csv'
pivot_df.to_csv(output_csv_path, index=False)
