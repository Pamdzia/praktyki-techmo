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

Skrypt bash przygotowujący datasety RAVDESS oraz nEMO wraz z ich pobraniem i uzyskaniem cech z wykorzystaniem MFCC znajduje się w *data-utils*, posiada on 5 zmiennych do ustalenia ściezek gdzie zostaną pobrane zipy z danymi, gdzie zapiszemy rozpakowane datasety oraz gdzie będą się znajdować csvki wynikowe, zarówno te pełne jak i pdozielone na sety train, dev, test.

Aby ręcznie przygotować zbiory należy:
- Wejść do folderu *data-utils*
- Uruchomić skrypt *data_downloader.py* podając ścieżkę do której chemy pobrać zbiory danych
- Uruchomić skrypt *Ravdess_csv_setter.py*, spowodowane jest to tym iż informacje o plikach znajdują się jedynie na stronie z datasetem, gdy nEMO pobierane jest wraz z plikiem .tsv
- Uruchomić skrypt *four_emotions_dataset_setup*, skrypt ten przygotowuje ujednolicenie nazw oraz wycięcie zbędnych cech
- Uruchomić skrypt *four_emotions_features_setup*, skrypt ten uruchamia analizę danych wyciągając features opisane w artykule
- Uruchomić skrypt *four_emotions_data_division*, skrypt ten odpowiada za podział korpusów na zbiory train, dev, test wykonując wyrównanie danych, aby w zbiorze testowym znajdowało się tyle samo próbek dla każdej emocji

# Tabele z danymi dla nEMO oraz RAVDESS podzielonymi na zbiory train, dev oraz test

## Podział zbioru danych RAVDESS (calm jako neutral)

## Original dataset distribution:
| Emotion | Count |
|---------|-------|
| Neutral | 376   |
| Happy   | 376   |
| Sad     | 376   |
| Angry   | 376   |

## Train dataset distribution:
| Emotion | Count |
|---------|-------|
| Neutral | 296   |
| Happy   | 296   |
| Sad     | 296   |
| Angry   | 296   |

## Dev dataset distribution:
| Emotion | Count |
|---------|-------|
| Neutral | 32    |
| Happy   | 32    |
| Sad     | 32    |
| Angry   | 32    |

## Test dataset distribution:
| Emotion | Count |
|---------|-------|
| Neutral | 48    |
| Happy   | 48    |
| Sad     | 48    |
| Angry   | 48    |

## Summary
Total number of files removed during balancing and equalizing: 0


## Podział zbioru danych nEMO

## Original dataset distribution:
| Emotion | Count |
|---------|-------|
| Neutral | 809   |
| Sad     | 769   |
| Happy   | 749   |
| Angry   | 749   |

## Train dataset distribution:
| Emotion | Count |
|---------|-------|
| Neutral | 578   |
| Sad     | 576   |
| Happy   | 570   |
| Angry   | 569   |

## Dev dataset distribution:
| Emotion | Count |
|---------|-------|
| Angry   | 90    |
| Happy   | 89    |
| Neutral | 86    |
| Sad     | 85    |

## Test dataset distribution:
| Emotion | Count |
|---------|-------|
| Happy   | 85    |
| Angry   | 85    |
| Sad     | 85    |
| Neutral | 85    |

## Summary
Total number of files removed during balancing and equalizing: 93

