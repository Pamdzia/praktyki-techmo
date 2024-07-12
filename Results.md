## co było brane pod uwagę podczas dzielenia modeli
- Przy wyborze najlepszych klasyfikatorów brano pod uwagę "classification rate", modele osiągające najwyższą średnią dokładność
  
## mini legenda
- klasyfikator_nEMO - model trenowany na zbiorze danych nEMO
- klasyfikator_RAVDESS - model trenowany na zbiorze danych RAVDESS
- klasyfikator_connected - model trenowany na obu (połączonych) zbiorach danych nEMO i RAVDESS
- klasyfikator_iemocap_connected - model treniwany na zbiorze danych IEMOCAP połączonych (gra aktorska i improwizacja)
- klasyfikator_iemocap_impro - model treniwany na zbiorze danych IEMOCAP improwizacyjnych
- klasyfikator_iemocap_script - model treniwany na zbiorze danych IEMOCAP skryptowych
- klasyfikator_emo_db - model treniwany na zbiorze danych emoDB (język niemicki)

## co oznaczaja wyniki (liczby) w tabelach
- "classification rates" obliczano, dzieląc całkowitą liczbę emocji należących do danej klasy w testowaniu przez całkowitą liczbę poprawnie rozpoznanych emocji tej klasy, jak pokazano poniżej:

$$
\frac{\text{Total number of correctly recognized emotions}}{\text{Total number of emotions}} \times 100\%
$$

# NAJLEPSZE WYNIKI DLA KNN 
- najlepsze wyniki dla zbioru danych RAVDESS uzyskał model kNN_connected
- najlepsze wyniki dla zbioru danych nEMO uzyskał model kNN_nEMO

## najlepszy wynik (oba zbiory testowe) dla kNN_connected
| Language       | Happiness | Sadness | Anger  | Neutral | Average |
|----------------|------------|---------|--------|---------|---------|
| Polish         | 45.88      | 77.65   | 36.47  | 41.18   | 50.30   |
| English        | 43.75      | 39.58   | 93.75  | 68.75   | 61.46   |
| Average        | 44.82      | 58.61   | 65.11  | 54.97   | 56.38   |


# NAJLEPSZE WYNIKI DLA KNN Z PREPROCESSINGIEM LDA
- najlepsze wyniki dla zbioru danych RAVDESS uzyskał model knn_lda_RAVDESS
- najlepsze wyniki dla zbioru danych nEMO uzyskał model knn_lda_nEMO

## najlepszy wynik (oba zbiory testowe) dla knn_lda_connected
| Language       | Happiness | Sadness | Anger  | Neutral | Average |
|----------------|-----------|---------|--------|---------|---------|
| Polish         | 31.76     | 64.71   | 44.71  | 30.59   | 42.94   |
| English        | 41.67     | 52.08   | 75.00  | 60.42   | 57.29   |
| Average        | 36.72     | 58.40   | 59.86  | 45.51   | 50.12   |

na podstawie: [link](https://www.researchgate.net/publication/318009355_Cognitive_Gravity_Model_Based_Semi-Supervised_Dimension_Reduction)

[wykres z tego artykułu](https://www.researchgate.net/figure/Accuracies-on-EmoDB-by-using-different-number-of-training-samples-where-KNN-is-utilized_fig5_318009355) 



# NAJLEPSZE WYNIKI DLA RANDOM FOREST
- najlepsze wyniki dla zbioru danych RAVDESS uzyskał model random_forest_connected
- najlepsze wyniki dla zbioru danych nEMO uzyskał model random_forest_emo_db

## najlepszy wynik (oba zbiory testowe) dla random_forest_connected
| Language       | Happiness | Sadness | Anger  | Neutral | Average |
|----------------|-----------|---------|--------|---------|---------|
| Polish         | 18.82     | 61.18   | 85.88  | 10.59   | 44.12   |
| English        | 33.33     | 60.42   | 81.25  | 54.17   | 57.29   |
| Average        | 26.08     | 60.80   | 83.57  | 32.38   | 50.70   |


# NAJLEPSZE WYNIKI DLA KNN Z PCA
- najlepsze wyniki dla zbioru danych RAVDESS uzyskał model knn_with_PCA_RAVDESS
- najlepsze wyniki dla zbioru danych nEMO uzyskał model knn_with_PCA_nEMO

## najlepszy wynik (oba zbiory testowe) dla knn_with_PCA_connected
| Language       | Happiness | Sadness | Anger  | Neutral | Average |
|----------------|-----------|---------|--------|---------|---------|
| Polish         | 35.29     | 71.76   | 31.76  | 30.59   | 42.85   |
| English        | 31.25     | 33.33   | 87.50  | 54.17   | 51.06   |
| Average        | 33.27     | 52.55   | 59.63  | 42.38   | 46.96   |


# NAJLEPSZE WYNIKI DLA SVC
- najlepsze wyniki dla zbioru danych RAVDESS uzyskał model SVC_RAVDESS
- najlepsze wyniki dla zbioru danych nEMO uzyskał model SVC_connected

## najlepszy wynik (oba zbiory testowe) dla SVC_connected
| Language       | Happiness | Sadness | Anger  | Neutral | Average |
|----------------|-----------|---------|--------|---------|---------|
| Polish         | 11.76     | 27.06   | 85.88  | 30.59   | 38.82   |
| English        | 50.00     | 62.50   | 91.67  | 54.17   | 64.08   |
| Average        | 30.88     | 44.78   | 88.78  | 42.38   | 51.45   |


# NAJLEPSZE WYNIKI DLA MLP_CLASSIFIER
- najlepsze wyniki dla zbioru danych RAVDESS uzyskał model mlp_RAVDESS
- najlepsze wyniki dla zbioru danych nEMO uzyskał model mlp_combined

## najlepszy wynik (oba zbiory testowe) dla SVC_connected
| Language       | Happiness | Sadness | Anger  | Neutral | Average |
|----------------|-----------|---------|--------|---------|---------|
| Polish         | 32.94     | 45.88   | 72.94  | 35.29   | 46.76   |
| English        | 56.25     | 58.33   | 89.58  | 60.42   | 66.65   |
| Average        | 44.60     | 52.10   | 81.26  | 47.85   | 56.70   |


# WNIOSKI
1. LDA w połączeniu z kNN daje lepsze wyniki (F1 = 71%) niż sam kNN (F1 = 51%) dla zbioru danych RAVDESS
2. Dane trenowane na zbiorze danych IEMOCAP zdecydowaną większość (lub całość) emocji ze zbioru RAVDESS i nEMO klasyfikują jako angry
3. zbiór RAVDESS często potrafi czerpać korzyści z trenowania na zbiorach RAVDESS i nEMO podczas gdy nEMO okazuje się dosyć opornym zbiorem danych do trenowania (ale ciężko znaleźć inny polski zbiór danych)
4. wykonano eksperyment trenowania modelu kNN ze znaleziona w interecie implementacją CGMSDR, model został po kolei sprawdzany dla każdej ilości cech PCA (od 1 do 75), najlepsze wyniki uzyskano dla 63 cech PCA, F1-score zbioru treningowego (trening na nEMO i RAVDESS) wyniósł 0.78, ale test tego modelu na zbiorze danych RAVDESS wyniósł jedynie 0.23 dla accuracy i F1 dlatego (biorąc pod uwagę wyniki pozostałych modeli) zdecydowano nie kontynuować eksperymentów na tym modelu (model ten uzyskał równie słabe wyniki wtedy, gdy dodatkowo (oprócz standaryzacji przed CGMSDR) dokonano normalizacji przed kNN)
