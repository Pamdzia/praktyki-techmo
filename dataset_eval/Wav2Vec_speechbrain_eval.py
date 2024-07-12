import pandas as pd
from tqdm import tqdm
from speechbrain.inference.interfaces import foreign_class

# Ścieżka do CSV z plikami dźwiękowymi
input_csv_path = "/Users/maciejwylecial/Developer/praktyki-Techmo/12_07/praktyki-techmo/four_emotions_csvs_all/four_emotions_nEMO_features.csv"
output_csv_path = "wav2vec_nEMO.csv"
base_audio_path = "/Users/maciejwylecial/Developer/praktyki-Techmo/12_07/praktyki-techmo/downloaded_data/nEMO/nEMO-main/samples/"

# Inicjalizacja klasyfikatora
classifier = foreign_class(
    source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",
    pymodule_file="custom_interface.py",
    classname="CustomEncoderWav2vec2Classifier"
)

# Wczytanie CSV
df = pd.read_csv(input_csv_path)

# Lista wyników do zapisania
results = []

# Funkcja do mapowania emocji
def map_emotion(emotion_list):
    emotion_map = {
        'hap': 'happy',
        'ang': 'angry',
        'neu': 'neutral',
        'sad': 'sad'
    }
    # Usunięcie nawiasów i cudzysłowów z listy
    emotion = emotion_list[0] if isinstance(emotion_list, list) and len(emotion_list) > 0 else emotion_list
    emotion = emotion.strip("[]' ")
    return emotion_map.get(emotion, emotion)

# Iteracja przez każdy wiersz CSV
for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    relative_path = row['relative path'].strip()
    true_emotion = row['emotion'].strip()
    audio_file_path = base_audio_path + relative_path

    # Klasyfikacja pliku dźwiękowego
    out_prob, score, index, text_lab = classifier.classify_file(audio_file_path)

    # Modyfikacja przewidywanej emocji
    predicted_emotion = map_emotion(text_lab)

    # Dodanie wyniku do listy
    results.append({
        "relative_path": relative_path,
        "true_emotion": true_emotion,
        "predicted_emotion": predicted_emotion
    })

# Zapisanie wyników do CSV
results_df = pd.DataFrame(results)
results_df.to_csv(output_csv_path, index=False)

print(f"Wyniki zostały zapisane do {output_csv_path}")
