import pandas as pd

# dane z datasetu po polsu
polish_data = pd.read_csv('filtered_nEMO_all.csv')
# dane z datsetu po ang (RAVDESS)
ravdess_data = pd.read_csv('filtered_RAVDESS_all.csv')

# analiza kolumny 'emotion' (pl)
polish_emotions = polish_data['emotion'].value_counts()
print("Polski dataset - emocje i ich ilości:")
print(polish_emotions)

# analiza kolumny 'emotion' (ang)
ravdess_emotions = ravdess_data['emotion'].value_counts()
print("\nDataset RAVDESS - emocje i ich ilości:")
print(ravdess_emotions)
