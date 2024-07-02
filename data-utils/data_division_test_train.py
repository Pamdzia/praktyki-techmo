import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_csvs\RAVDESS_features_all.csv')

# wyciagniecie unikalnych file_id
df['context_speaker_id'] = df['file_id'].apply(lambda x: x.split('/')[0])

#  na zbiory treningowy (80%) i testowy (20%)
train_ids, test_ids = train_test_split(df['context_speaker_id'].unique(), test_size=0.2, random_state=42)

# filtrowanie danych na podstawie context_speaker_id
def filter_by_ids(df, ids):
    return df[df['context_speaker_id'].isin(ids)]

train_df = filter_by_ids(df, train_ids)
test_df = filter_by_ids(df, test_ids)

print("Train dataset distribution:")
print(train_df['emotion'].value_counts())
print("Test dataset distribution:")
print(test_df['emotion'].value_counts())

# zapisanie
train_df.to_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_division\test-train\train_ravdess.csv', index=False)
test_df.to_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_division\test-train\test_ravdess.csv', index=False)
