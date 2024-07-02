import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_csvs\nEMO_features_all.csv')

# unikalne fileid
df['context_speaker_id'] = df['file_id'].apply(lambda x: x.split('/')[0])

# zbiory treningowy (70%), walidacyjny (15%) i testowy (15%)
train_ids, temp_ids = train_test_split(df['context_speaker_id'].unique(), test_size=0.3, random_state=42)
dev_ids, test_ids = train_test_split(temp_ids, test_size=0.5, random_state=42)

# filtrowanie danych na podstawie context_speaker_id
def filter_by_ids(df, ids):
    return df[df['context_speaker_id'].isin(ids)]

train_df = filter_by_ids(df, train_ids)
dev_df = filter_by_ids(df, dev_ids)
test_df = filter_by_ids(df, test_ids)

print("Train dataset distribution:")
print(train_df['emotion'].value_counts())
print("Dev dataset distribution:")
print(dev_df['emotion'].value_counts())
print("Test dataset distribution:")
print(test_df['emotion'].value_counts())

train_df.to_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_division\test-train-dev\train_nemo.csv', index=False)
dev_df.to_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_division\test-train-dev\dev_nemo.csv', index=False)
test_df.to_csv(r'C:\Users\Asus\Desktop\PRAMCOWY_PROJEMKT\praktyki-techmo\data_division\test-train-dev\test_nemo.csv', index=False)
