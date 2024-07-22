Aby ręcznie przygotować zbiory należy:
- Wejść do folderu *data-utils*
- Uruchomić skrypt *data_downloader.py* podając ścieżkę do której chemy pobrać zbiory danych
- Uruchomić skrypt *Ravdess_csv_setter.py*, spowodowane jest to tym iż informacje o plikach znajdują się jedynie na stronie z datasetem, gdy nEMO pobierane jest wraz z plikiem .tsv
- Uruchomić skrypt *four_emotions_dataset_setup*, skrypt ten przygotowuje ujednolicenie nazw oraz wycięcie zbędnych cech
- Uruchomić skrypt *four_emotions_features_setup*, skrypt ten uruchamia analizę danych wyciągając features opisane w artykule
- Uruchomić skrypt *four_emotions_data_division*, skrypt ten odpowiada za podział korpusów na zbiory train, dev, test wykonując wyrównanie danych, aby w zbiorze testowym znajdowało się tyle samo próbek dla każdej emocji
