# Praktyki w Techmo

# Temat pracy

**Badanie różnic w klasyfikacji emocji między językiem polskim, a językiem angielskim**

# Motywacja

Ninejszy projekt bazowany jest na artykule: 
[Influences of languages in speech emotion recognition: A comparative study using Malay, English and Mandarin languages](https://ieeexplore.ieee.org/document/7575033/authors#authors), autorstwa **Rajesvary Rajoo** oraz **Ching Chee Aun**.

# Dane

Do pracy nad emocjami wykorzystywane są dane z niniejszych zbiorów 

Główne zbiory eksperymentu badania różnic między polskim i angielskim wykorzystywane do treningów oraz do wszystkich testów:
- [RAVDESS](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio) - Język angielski
- [nEMO](https://huggingface.co/datasets/amu-cai/nEMO) - Język polski

Zbiór w języku niemieckim do treningu modeli bazując na innym języku niż testowane, zgodnie z artykułem:
- [emoDB](https://www.kaggle.com/datasets/piyushagni5/berlin-database-of-emotional-speech-emodb) - Język niemiecki

Zbiór w języku angielskim, aby zobaczyć czy cechy języka są podobne:
- [TESS](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess) - Język angielski
  
Dodatkowe zbiory treningowe 
- [IEMOCAP](https://sail.usc.edu/iemocap/) - Język angielski
- [SAVEE](https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee) - Język angielski
- [JL-Corpus](https://www.kaggle.com/datasets/tli725/jl-corpus) - Język angielski
- [MSP_Podcast](https://ecs.utdallas.edu/research/researchlabs/msp-lab/MSP-Podcast.html) - Język angielski

# 1. Przygotowanie środowiska do pracy

Napisano skrypt *install.sh* [pełny skrypt](https://github.com/Pamdzia/praktyki-techmo/blob/main/install.sh), który przygotowuje wirtualne środowisko pythona 3.10 oraz korzysta z *setup.py* [pełny skrypt](https://github.com/Pamdzia/praktyki-techmo/blob/main/setup.py), który konfiguruje pakiet Python o nazwie 'praktyki-techmo' w wersji 0.9, wyszukuje i dołącza wszystkie jego podpakiety oraz instaluje wymagane zależności wymienione w pliku 'requirements.txt'.

Aby przygotować projekt należy wykonać poniższe kroki:

```bash
git clone https://github.com/Pamdzia/praktyki-techmo.git
cd praktyki-techmo
./install.sh
```

Instalacja środowiska może potrwać do kilku minut w zaleźności od szybkości transferu po instalacji powinna się pojawić informacja w terminalu:

```bash
Proszę pamiętać o włączeniu środowiska wirtualnego
```

Skrypt generuje środowisko wirtualne które można znaleźć pod nazwa `.venv` w katalogu głównym, aby je uruchomić musimy zastosować:

Dla systemów Unix/MacOS:

```bash
source .venv/bin/activate
```

Natomiast dla systemu Windows:

```powershell
.\.venv\Scripts\activate
```

Jeśli uruchomienie środowiska się powiodło w terminalu powinna wyświetlać się nazwa środowisko wirtualnego w tym przypadku `.venv`:

```bash
(.venv) praktyki-techmo % 
```

# 2. Przygotowanie danych

Podstawowe ustawienie zbiorów danych pod dalszą pracę jest wykonywane z wykorzytaniem skryptów [dataset_setup.sh](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-utils/datasets_setup.sh) oraz [dataset_setup_win.ps1](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-utils/dataset_setup_win.ps1) w zależności od wykorzystywanego systemu Ubuntu/MacOS lub Windows 

Aby uruchomić skrypty przygotowujące dane należy przejść do folderu folderu `data-utils` w którym znajdują się potrzebne narzędzia do przygotowania zbiorów danych, zbiory nEMO oraz RAVDESS są dostępne do pobrania i przekształcenia, natomiast emoDB, który także był wykorzystywany do wszystkich treningów jest dostępny po zalogowaniu na stronie Kaggle do ręcznego pobrania. Do przygotowania podstawowych zbiorów danych z tego ekseprymentu należy:

Przejść do katalogu z narzędziami, załóżmy, że znajdujemy się w katalogu głównym `praktyki-techmo`:

```bash
cd data-utils
```

Następnie należy uruchomić skrypt odpowiedni dla systemu operacyjnego::

Unix/MacOS:
```bash
./datasets_setup.sh
```

Windows:

```powershell
.\dataset_setup_win.ps1
```

W terminalu można zobaczyć postęp prac od paska postępu przy pobieraniu korpusów, ekstrakcji cech, aż po wyświetlenie finalnych tabel z ilością nagrać dla każdej emocji oraz informacją ile nagrań zostało usuniętych, tak wygląda ostatnie 8 wierszy po zakończonym procesie:

```bash
Test dataset distribution:
emotion
happy      85
angry      85
sad        85
neutral    85
Name: count, dtype: int64
Total number of files removed during balancing and equalizing: 93
```

Zbiór emoDB, zresztą jak i RAVDESS oraz nEMO ma wyciągnięte już features i jest zapisany w [four_emotions_csvs_all](https://github.com/Pamdzia/praktyki-techmo/tree/main/four_emotions_csvs_all) umożliwiając podział go na zbiory train, dev i test bez potrzeby wyciągania cech z nagrań, podzielone wstępnie zostały zbiory nEMO, RAVDESS, emoDB oraz iemocap do którego dostęp należy uzyskać kontaktując się z twórcami. Jednakże zostały przygotowane skrypty do własnoręcznego odtwrozenia ekseprymentu dla emoDB, znajduje się plik [tekstowy](https://github.com/Pamdzia/praktyki-techmo/blob/main/downloaded_data/emoDB/emoDB-download-manual.txt) znajduje się w nim link do strony na Kaggle ze zbiorem do pobrania wraz z informacją że należy folder z pobranymi plikami wav skopiować do folderu w którym znajduje się owy plik. Po skopiowaniu danych do folderu, aby przygotować ręcznie zbiory dla emoDB użytkownik poiwnien uruchomić skrypt znajdujący się analogicznie do poprzednich w `data-utils`.

```bash
emoDB_setup.sh
```

Sytuacja ze zbiorem TESS jest analogiczna do zbioru emoDB, jest on dostepny do pobrania na kaggle a samo przygotowanie również wygląda podobnie, należy folder z danymi wrzucić do folderu TESS zgodnie z instrukcją z pliku [tekstowego](https://github.com/Pamdzia/praktyki-techmo/blob/main/downloaded_data/TESS/TESS-download-manual.txt), co do skryptu przygotowującego dataset należy uruchomin ponownie będąc w folderze `data-utils`:

```bash
TESS_setup.sh
```

Pipeline do konfigurowania zbiorów nEMO/RAVDESS wygląda następująco (pipeline dla emoDB i TESS korzysta z nieco zmodyfikowanych skryptów csv_setter oraz dataset_setup, gdzie dla zbioru TESS nie ma podziału na sety, jest tylko jeden duży w pełni zbalansowany pod względem emocji zbiór użyty do treningu)
## Skrypt data_downloader
- Pobranie podstawowych zbiorów danych (RAVDESS oraz nEMO)
- Rozpakowanie pobranych nagrań do odpowiednich folderów
## Skrypt RAVDESS_csv_setter
- Przygotowanie pliku csv dla zbioru RAVDESS, nEMO jest pobierany wraz z plkiem z informacjami natomiast csv dla RAVDESS jest prazygotowywane zgodnie z informacjami ze strony datasetu na [Kaggle](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
## Skrypt four_emotions_datasets_setup
- Przygotowanie plików csv definiujących zbiory danych mapując zgodnie poszczególne cechy wraz z przygotowaniem czterech podstawowych emocji angry, sad, happy oraz neutral
## Skrypt four_emotions_features_setup
- Wczytywanie plików csv definiujących zbiory danych tak aby zmapować emocję z odpowiednim nagraniem
- Wyciągnięcie cech z nagrań (z ich wartościami mean, var, max, min, range) obejmujących: po 12 cech MFCC, pitch, energy, zcr
## Skrypt four_emotions_data_division
- Wczytanie pełnych plików csv z wyekstrachowanymi cechami
- Podzielenie korpusu na zbiory train, test, dev wykonując balansowanie ilości nagrań z naciskem na wyrównany podział emocji w zbiorze testowym, w przybliżeniu zbiory zostały podzielone (train/dev/test) w ilościach (573/87/85) w języku polskim nEMO, (296/32/48) w języku angielskim RAVDESS i (51/7/4) w języku niemieckim emoDB
- [dokładne liczby znajdują się w pliku Data.md](https://github.com/Pamdzia/praktyki-techmo/blob/main/Data.md)
## W razie potrzeby użytkownik może również ręcznie uruchomić pojedyncze skrypty, bądź przekształcić je pod inne zbiory danych, instrukcja dla poszczególnych skryptów znajduje się [tutaj](https://github.com/Pamdzia/praktyki-techmo/blob/main/Manual.md)

# 3. Przygotowanie danych do treningu i trening modeli 

Dane zostały w każdym pliku osobno przygotowane do treningu (konwersja określonych kolumn danych na tablice numpy, usunięcie białych przestrzeni, label encoder, przygotowanie train, (dev w przypadku MLP) i test data, użycie StandartScaler). Następujące modele: MLP_from_git_updated - model Sequential z warstwami Dense i Dropout, MLP_from_git_updated2 - model Sequential z warstwami Dense, Dropout i BatchNormalization, SVC, SVC z LDA, SVC z PCA, kNN, kNN z LDA, kNN z PCA, MLPClassifier, random forest) zostały napisane i wytrenowane osobno dla każdego ze zbiorów danych: nEMO, RAVDESS, nEMO + RAVDESS, emoDB. Dla każdego modelu wybrano odpowiednie hiperparametry korzystając z siatki grid search. Dodatkowo wybrane modele zostały wytrenowane na zbiorze danych IEMOCAP ale z powodu niezadowalających wyników testowych nie kontynuowano pracy z tym zbiorem danych. Każdy wytrenowany model zapisano.

- kody modeli znajdują się w folderze [training_model](https://github.com/Pamdzia/praktyki-techmo/tree/main/training_model) wszystkie zapisane modele znajdują się w odpowiednio nazwanych podfolderach folderu training_model
- dodatkowo wytrenwano modele na zbiorze danych TESS po 400 plików dla każdej z emocji "sad", "neutral", "happy", "angry", gotowe wytrenowane modele znajdują się w folderze [TESS_models](https://github.com/Pamdzia/praktyki-techmo/tree/main/TESS_models)

# 4. Testowanie wytrenowanych modeli i wyniki

## 4.1. Skrypty testujące modele:

Do uruchomienia podstawowego pipeline testowego (wykonanie testów na wszystkich modelach znajdujących się w folderze) należy przejść do folderu *training_model* oraz uruchomić skrypt [testing_pipeline](https://github.com/Pamdzia/praktyki-techmo/blob/main/training_model/testing_pipeline.sh) 

Zakładając, że ścieżką podstawową jest główny katalog `praktyki-techmo`, aby uruchomić testy można skorzystać z: (zarówno pipeline testujący jak i przygotowanie zbioru emoDB zostały przygotowane tylko dla systemów Unix/MacOS z pominięciem skryptów powershell dla Windowsa)

```bash
cd treining_model
./testing_pipeline.sh
```

skrypt ten uruchamia testy na wszystkich modelach dodając od razu zbiory testowe dla języka polskiego oraz angielskiego, pipeline korzysta z [testing](https://github.com/Pamdzia/praktyki-techmo/blob/main/training_model/testing.py) który odpowiada za logikę uruchamiania zapisanych model iz checkpointów, rozróżniając po nazwach co należy wczytać. Skrypt kalkuluje metryki, generuje macierz pomyłek zapisując wyniki domyślnie w folderze experiments_results w ustawionej dla danego eksperymentu nowym folderze. Generowane pliki to zbiorcze pliki csv z wynikami znajdujące się w folderze ogólnym wyników eksperymentów oraz poszczególne pliki w fodlerze eksperymentu zawierające f1-score oraz pliki zapisywane osobno dla każdego z modeli pod ppojedynczy zbiór testowy w skład których wchodzą classification report z wynikami dla każdej emocji, confusion matrix w formie csv oraz confusion matrix w formie graficznej. 

**Dodatkowe skrypty do badań oraz testów również na transformerach jak i dokładna instrukcja tłumacząca zmienne w skrypcie znajduje się [tutaj](https://github.com/Pamdzia/praktyki-techmo/blob/main/Manual.md)**

## 4.2. Testy modeli oraz wyniki

Przetestowano wszystkie wytrenowane modele na zbiorach danych nEMO i RAVDESS. Wyniki najlepszych modeli i wnioski, które z nich wynikały wypisano w pliku [Results.md](https://github.com/Pamdzia/praktyki-techmo/blob/main/Results.md). Dla najlepszych modeli wypisano także Classification Report znajdujące się w pliku [ClassificationReports.md](https://github.com/Pamdzia/praktyki-techmo/blob/main/ClassificationReports.md), a macierze pomyłek w pliku [ConfusionMatrixes.md](https://github.com/Pamdzia/praktyki-techmo/blob/main/ConfusionMatrixes.md). Wszystkie wyniki classification report i confusion matrix znajdują się w [folderze](https://github.com/Pamdzia/praktyki-techmo/blob/main/ConfusionMatrixes.md) (nazwa_modelu_zbior_na_ktorym_train_zbior_test). Dodatkowo całość dla zbioru nEMO i RAVDESS znajdują się pod linkami: [nEMO](https://github.com/Pamdzia/praktyki-techmo/blob/main/experiments_results/test_results_1507_nEMO.csv), [RAVDESS](https://github.com/Pamdzia/praktyki-techmo/blob/main/experiments_results/test_results_1507_RAVDESS.csv). Wyniki F1 score dla każdego modelu znajdują się w pliku [ModelsF1Comparasion.md](https://github.com/Pamdzia/praktyki-techmo/blob/main/ModelsF1Comparasion.md)

wyniki dla modeli trenowanych na zbiorze danych TESS znajdują się w folderze [TESS](https://github.com/Pamdzia/praktyki-techmo/tree/main/experiments_results/TESS) w experiments_results

## 4.3. Inferencja modelu

Aby przetestować dowolny z wytrenowanych modeli (posiadających nazwę zgodną z tym jaka to architektura modelu) należy uruchomić skrypt [simple_inference](https://github.com/Pamdzia/praktyki-techmo/blob/main/simple_inference.py) znajdujący się w katalogu głównym projektu. Skrypt ten przyjmuje dwa argumenty wejściowe --model_dir gdzie podaje się ścieżkę do folderu z modelem oraz --audio_path gdzie podawana jest ścieżka do pliku .wav, jeśli nazwa modelu jest zgodna z typem architektury skrypt na jej podstawie wczyta wszystkie wymagane pliki .pkl z folderu modelu

Przykład jak wykonać inferencję, na jednym z gotowych modeli wykorzystując jedno z przykładowych nagrań, nagrania te są bazowane na zbiorze testowym RAVDESS i są jedną przykładową emocją, można jest znaleźć w [test_recordings](https://github.com/Pamdzia/praktyki-techmo/tree/main/test_recordings)

```bash
python simple_inference.py --model_dir training_model/knn_RAVDESS --audio_path test_recordings/angry.wav
```

Po uruchomieniu komendy użytkownik powinien zobaczyć wynik detekcji emocji:

```bash
Predykowana emocja: angry
```


# 5. Wnioski

Napisano skrypt [best-emotions.py](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/best-emotions.py), który umożlwia uzyskanie plików opisujących najlepiej i najgorzej (poniżej 0.2) wykrywane emocje dla każdego modelu na podstawie precision, recall i f1-score. Uzyskane pliki znajdują się w folderze [data-testing](https://github.com/Pamdzia/praktyki-techmo/tree/main/data-testing), nazwy plików zaczynają się od precision/recall/f1-score, RAVDESS i nEMO to nazwa zbioru na których modele były testowane, dodatkowa nazwa emo_DB oznacza, że modele były trenowane na tym zbiorze danych. 

- dokładny opis plików z precision i wnioski końcowe znajdują się w pliku [SummaryUpdated.md](https://github.com/Pamdzia/praktyki-techmo/blob/main/SummaryUpdated.md)

# WNIOSEK KOŃCOWY
Język ma wpływ na skuteczność rozpoznawania emocji, co jest widoczne w tendencji, że modele trenowane na jednym języku mają ogromne trudności z rozpoznawaniem emocji w innym języku co może być spowodowane tym, że dane były z dwóch zupełnie innych zbiorów. Zbiory trenowane na jednym zbiorze, a testowane na drugim radziły sobie nienajgorzej z emocją "sad" co może dowodzić temu, że emocja smutku wyrażana w obu językach posiada podobne cechy. Modele wykazują wyższą skuteczność, gdy są trenowane i testowane na tym samym zbiorze danych (szczególnie dla zbioru danych w języku angielskim), jest to naturalne zjawisko aczkolwiek zbyt niskie wyniki (praktycznie zerowa precyzja w każdym modelu dla happy i neutral testowanych na języku angielskim i trenowanym na języku polskim) mogą świadczyć również o tym, że cechy emocji wyrażanych w obu językach są inne.

Na podstawie wyników testów (język polski i angielski) modeli trenowanych na języku niemieckim można zauważyć, że w przypadku języka polskiego najlepiej rozpoznawaną emocją jest emocja smutku, potrafiła ona w 5 eksperyemtach osiagnąc precyzję równą 1, emocja złości uzyskiwała niską precyzję w wielu eksperymentach, tylko w jednym (random_forest_emo_db uzyskała precyzję pozwyżej 0.5) Podczas testowania na języku angielskim najlepsze wyniki uzyskano dla emocji złości. Emocja smutku natomiast wynosiła ponizej 0.2 w większości z eksperymentów, z tego wynika, że o ile emocja smutku zawiera podobne cechy w języku polskim i angielskim, cechy te różnią się na tyle, że podczas testowania na modelach, które były trenowane na innym języku emocja ta nie jest rozpoznawana w obu przypadkach.

Podczas testowania zbiorów nEMO i RAVDESS na modelach trenowanych na zbiorze danych TESS można zauważyć, że zarówno angielski jak i polski zbiór danych najelpiej radzi sobie dla emocji smutku, co może potwierdzać to, że oba języki posiadają najbardziej zbliżone cechy dla tej właśnie emocji. Modele testowane na zbiorze danych RAVDESS osiągały także nienajgorsze wyniki dla emocji "neutral", zgadza się to z wynikami modeli trenowanych i testowanych na zbiorze danych RAVDESS. Wyniki na tym drugim oczywiście są wyższe, co jest naturalnym zjawiskiem dla modeli trenowanych i testowanych na tym samym zbiorze danych. Modele testowane na zbiorze danych nEMO uzyskały lepsze wyniki precyzji (dla emocji smutku) dla modeli trenowanych na zbiorze danych TESS niż na zbiorze danych RAVDESS.


