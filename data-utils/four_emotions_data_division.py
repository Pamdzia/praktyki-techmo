import os
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse

# Argumenty wiersza poleceń
parser = argparse.ArgumentParser(description='Podział danych na zbiory treningowy, walidacyjny i testowy.')
parser.add_argument('--csv_path', default='../four_emotions_csvs_all/four_emotions_RAVDESS_features.csv', help='Ścieżka do pliku CSV z danymi')
parser.add_argument('--output_dir', default='../four-emotions-csv-sets', help='Katalog wyjściowy na pliki z danymi')

args = parser.parse_args()

# Ścieżki
CSV_PATH = args.csv_path
OUTPUT_DIR = args.output_dir

# Ścieżka do pliku wyjściowego na podstawie nazwy ścieżki wejściowej
csv_filename = os.path.basename(CSV_PATH)

train_output_filename = 'train_' + csv_filename
dev_output_filename = 'dev_' + csv_filename
test_output_filename = 'test_' + csv_filename

TRAIN_OUTPUT_PATH = os.path.join(OUTPUT_DIR, train_output_filename)
DEV_OUTPUT_PATH = os.path.join(OUTPUT_DIR, dev_output_filename)
TEST_OUTPUT_PATH = os.path.join(OUTPUT_DIR, test_output_filename)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

df = pd.read_csv(CSV_PATH)

# unikalne context_speaker_id
df['context_speaker_id'] = df['actor']

# sprawdzenie rozkładu klas przed balansowaniem
print("Original dataset distribution:")
print(df['emotion'].value_counts())

# balansowanie klas w zbiorze danych
def balance_classes(df):
    class_counts = df['emotion'].value_counts().to_dict()
    min_class_count = min(class_counts.values())
    
    balanced_df = pd.concat([
        df[df['emotion'] == cls].sample(min_class_count, random_state=42)
        for cls in class_counts.keys()
    ])
    
    return balanced_df, len(df) - len(balanced_df)

# zbiory treningowy (80%), walidacyjny (10%) i testowy (10%) -- uniklanli speakerzy!!
def split_data(df):
    speakers = df['context_speaker_id'].unique()
    if len(speakers) < 3:
        raise ValueError("Not enough unique speakers to split into train, dev, and test sets.")
    
    train_speakers, temp_speakers = train_test_split(speakers, test_size=0.2, random_state=42)
    dev_speakers, test_speakers = train_test_split(temp_speakers, test_size=0.5, random_state=42)

    train_df = df[df['context_speaker_id'].isin(train_speakers)]
    dev_df = df[df['context_speaker_id'].isin(dev_speakers)]
    test_df = df[df['context_speaker_id'].isin(test_speakers)]

    return train_df, dev_df, test_df

# balansowanie i podział
balanced_df, num_removed_files = balance_classes(df)
train_df, dev_df, test_df = split_data(balanced_df)

# funkcja ktora wyrownuje klasy w zbiorze testowym
def equalize_test_set(test_df, train_df, dev_df):
    class_counts = test_df['emotion'].value_counts()
    min_class_count = class_counts.min()
    
    # redukcja przykladow w zbiorze testowym
    equalized_test_df = pd.concat([
        test_df[test_df['emotion'] == cls].sample(min_class_count, random_state=42)
        for cls in class_counts.keys()
    ])
    
    num_removed_test_files = len(test_df) - len(equalized_test_df)

    # dodanie brakujących przykładów z dev lub train do zbioru testowego
    for cls in class_counts.keys():
        while len(equalized_test_df[equalized_test_df['emotion'] == cls]) < min_class_count:
            if not dev_df[dev_df['emotion'] == cls].empty:
                sample = dev_df[dev_df['emotion'] == cls].sample(1, random_state=42)
                dev_df = dev_df.drop(sample.index)
            elif not train_df[train_df['emotion'] == cls].empty:
                sample = train_df[train_df['emotion'] == cls].sample(1, random_state=42)
                train_df = train_df.drop(sample.index)
            equalized_test_df = pd.concat([equalized_test_df, sample])
    
    return equalized_test_df, train_df, dev_df, num_removed_test_files

# wyrównanie zbioru testowego
test_df, train_df, dev_df, num_removed_test_files = equalize_test_set(test_df, train_df, dev_df)

# sprawdzenie unikalności speakerów
def check_unique_speakers(train_df, dev_df, test_df):
    train_speakers = set(train_df['context_speaker_id'])
    dev_speakers = set(dev_df['context_speaker_id'])
    test_speakers = set(test_df['context_speaker_id'])

    assert train_speakers.isdisjoint(dev_speakers), "Train and Dev sets have overlapping speakers"
    assert train_speakers.isdisjoint(test_speakers), "Train and Test sets have overlapping speakers"
    assert dev_speakers.isdisjoint(test_speakers), "Dev and Test sets have overlapping speakers"
    print("All speakers are unique across the sets")

check_unique_speakers(train_df, dev_df, test_df)

train_df.to_csv(TRAIN_OUTPUT_PATH, index=False)
dev_df.to_csv(DEV_OUTPUT_PATH, index=False)
test_df.to_csv(TEST_OUTPUT_PATH, index=False)

print("Train dataset distribution:")
print(train_df['emotion'].value_counts())
print("Dev dataset distribution:")
print(dev_df['emotion'].value_counts())
print("Test dataset distribution:")
print(test_df['emotion'].value_counts())

total_removed_files = num_removed_files + num_removed_test_files
print(f"Total number of files removed during balancing and equalizing: {total_removed_files}")
