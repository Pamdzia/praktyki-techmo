# Instrukcja skryptów

**Uwaga, przed dalszą pracą należy uruchomić skrypt install.sh który koniguruje środowisko, następnie zgodnie z informacją w terminalu uruchomic powstałe środowisko wirtualne**

# Kolejność przygotowania danych:

Aby ręcznie przygotować zbiory należy:
- Wejść do folderu *data-utils*
- Uruchomić skrypt *data_downloader* podając ścieżkę do której chemy pobrać zbiory danych można to zrobić zmieniając argumenty ustawione jako *default* w skrypcie, bądź podając przy uruchamianiu argumenty gdzie rozpakujemy dane oraz gdzie powinny znajdować się pobrane zipy
- Uruchomić skrypt *Ravdess_csv_setter.py*, spowodowane jest to tym iż informacje o plikach znajdują się jedynie na stronie z datasetem, gdy nEMO pobierane jest wraz z plikiem .tsv, jeśli ścieżka zapisu została zmieniona należy to uwzględnić uruchamiając skrpyt zmieniając wartość default bądź podając nową ścieżkę w argumencie wejściowym
- Uruchomić skrypt *four_emotions_dataset_setup*, skrypt ten przygotowuje ujednolicenie nazw oraz wycięcie zbędnych cech, analogicznie do poprzednich, jeżeli nastąpiła zmiana ścieżek zapisu należy uwzględnić je w wartościach default bądź podać jako argumenty weściowe nowe ścieżki do plików .csv oraz .tsv dla nEMO
- Uruchomić skrypt *four_emotions_features_setup*, skrypt ten uruchamia analizę danych wyciągając features opisane w artykule, skrypt jest przystosowany do analizy pojedynczego zbioru jeśli użytkownik chce wyciągać cechy z wielu zbiorów powinien uruchamiać je kolejno podając odpowiedni ścieżki dla każdego uruchomienia, może to być zrealizowane skryptem bash stąd zarówno ścieżka do danych wejściowych, do csv oraz ścieżka do wyściowej csvki jest podawana przez argument, nazwa pliku wyjściowego jest bazowana na nazwie wejściowego pliku .csv, ponownie jeśli ścieżki są nowe należy to uwzględnić w argumentach, dodatkowo pojawia się argument *--output_dir* który odpowiada za zapis pełnych plików .csv z wyekstrachowanymi cechami
- Uruchomić skrypt *four_emotions_data_division*, skrypt ten odpowiada za podział korpusów na zbiory train, dev, test wykonując wyrównanie danych, aby w zbiorze testowym znajdowało się tyle samo próbek dla każdej emocji, również ten skrypt jest uruchamiany z osobna dla każdego zbioru argumentami są plik zawierający pełen zbiór w formacie .csv oraz ścieżka gdzie powinny zbiory train, dev i test zostać zapisane, ścieżka wyściowa jest bardzo ważna gdyż wszystkie skrpyty domyślnie są ustawione do korzystania z relatywnych ścieżek do folderu *four-emotions-csv-sets* gdzie zpaisywane są pliki uruchamiane z wykorzystaniem skryptów *pipeline* 

# Uruchamianie treningów:

Aby ręcznie uruchomić treningi należy:
- Wejść do folderu *training_model*
- Uruchomić dowolny skrypt treningowy znajdujący się w folderze, w każdym z nich są zdefiniowane nazwy *default_experiment_name*, użytkownik może ustawić go pod siebie ale dobrą praktyką byłoby zostawienie w nazwie jaki to trening, preprocesing jeśli takowy jest używany oraz nazwę zbioru danych czy to emoDB, czy to RAVDESS albo jakikolwiek inny, bądź połączenie takowych zbiorów, pozwala to na bezproblemowe uruchamianie testów dla wszstskich mdoeli które zostały wytrenowane
- Ustawić ścieżki do zbiorów treningowych oraz testowych, domyślnie zbiory te znajdują się w *four-emotions-csv-sets* stąd ścieżki w skryptach mogą być skrócone do relatywnych kierujących do tego folderu
- W każdym treningu znajduje się grid search, sprawdzający wszystkie zdefiniowane dla treningu hiperparametry, jeśli użytkownik chce sprawdzić dodatkowe parametry może to zrobić dodając jest do *param_grid* w kodzie wybranego treningu

# Testowanie wytrenowanych modeli:

Aby przetestować modele mnależy:
- Wejść do folderu *training_model*
- Uruchomić skrypt *testing* w skrypcie tym można zdefiniować kilka emlementów, użytkownik jest w stanie zmienić nazwę ekseprymentu w *experiment*, jest to nazwa folderu do którego będą zapisywane szczegółowe wyniki dla poszczególnego modelu na pojedynczym zbiorze testowym, w skład tego wchodzą classification report, confusion matrix oraz łączone f1 dla wszystkich modeli które są testowane pod jedną nazwą eksperymentu, główny folder z wynikami jest opisany jako *results_folder*, natomiast argumentem wejściowym dla skryptu są, nazwa datasetu testowego oraz nazwa eksperymentu w kontekście treningu (patrz punkt wyżej *Uruchamianie treningów*)

Dodatkowy krok pozwalający na wyciągnięcie wyników dla poszczególnych emocji w formie wypisywania najlepszej detekcji dal danego modelu, jakie emocje są poprawnie wykrywane (wartość accuracy >0.5) oraz które emocje są bardzo źle wykrywane (wartość accuracy <0.2), aby wykonać ten test należy:
- Wejść do folderu *data-testing*
- Uruchomić skrypt best-emotions.py podając ścieżkę do pliku .csv ze zbiorczymi wynikami testów dla zbioru który nas interesuje na przykład [test_results_1507_RAVDESS.csv](https://github.com/Pamdzia/praktyki-techmo/blob/main/experiments_results/test_results_1507_RAVDESS.csv), korzystając ze zmiennej *file_path*
- Wyniki są zapoisywane w plikach testowych dla kilke metryk takich jak f1, recall oraz precision, a same pliki tworzone są w ścieżce gdzie znajduje się skrypt tj. *data-testing*

# Dodatkowe skrypty pozwalające na inne pomniejsze testy lub sprawdzanie zbiorów

