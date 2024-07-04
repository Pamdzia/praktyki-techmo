# Praktyki w Techmo

# Temat pracy

**Badanie różnic w klasyfikacji emocji między językiem polskim, a językiem angielskim**

# Motywacja

Ninejszy projekt bazowany jest na artykule: 
[Influences of languages in speech emotion recognition: A comparative study using Malay, English and Mandarin languages](https://ieeexplore.ieee.org/document/7575033/authors#authors), autorstwa **Rajesvary Rajoo** oraz **Ching Chee Aun**.

# Dane

Do pracy nad emocjami wykorzystywane są dane z niniejszych zbiorów 
- [IEMOCAP](https://sail.usc.edu/iemocap/) - Język angielski
- [RAVDESS](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio) - Język angielski
- [TESS](https://tspace.library.utoronto.ca/handle/1807/24487) - Język angielski
- [SAVEE](https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee) - Język angielski
- [JL-Corpus](https://www.kaggle.com/datasets/tli725/jl-corpus) - Język angielski
- [MSP_Podcast](https://ecs.utdallas.edu/research/researchlabs/msp-lab/MSP-Podcast.html) - Język angielski
- [nEMO](https://huggingface.co/datasets/amu-cai/nEMO) - Język polski

# Przygotowanie danych

Skrypt bash przygotowujący datasety RAVDESS oraz nEMO wraz z ich pobraniem i uzyskaniem cech z wykorzystaniem MFCC jest podstawą issue #9. Aby ręcznie przygotować zbiory należy:
- Wejść do folderu *data-utils*
- Uruchomić skrypt *data_downloader.py* podając ścieżkę do której chemy pobrać zbiory danych
- Uruchomić skrypt *Ravdess_csv_setter.py*, spowodowane jest to tym iż informacje o plikach znajdują się jedynie na stronie z datasetem, gdy nEMO pobierane jest wraz z plikiem .tsv
- Uruchomić skrypt *four_emotions_dataset_setup*, skrypt ten przygotowuje ujednolicenie nazw oraz wycięcie zbędnych cech
- Uruchomić skrypt *four_emotions_features_setup*, skrypt ten uruchamia analizę danych wyciągając features opisane w artykule
- Uruchomić skrypt *four_emotions_data_division*, skrypt ten odpowiada za podział korpusów na zbiory train, dev, test wykonując wyrównanie danych, aby w zbiorze testowym znajdowało się tyle samo próbek dla każdej emocji

# Tabele z danymi dla nEMO oraz RAVDESS podzielonymi na zbiory train, dev oraz test
