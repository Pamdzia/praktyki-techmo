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


# WNIOSKI
1. LDA w połączeniu z kNN daje lepsze wyniki (F1 = 71%) niż sam kNN (F1 = 51%) dla zbioru danych RAVDESS
2. Dane trenowane na zbiorze danych IEMOCAP zdecydowaną większość (lub całość) emocji ze zbioru RAVDESS i nEMO klasyfikują jako angry
3. zbiór RAVDESS często potrafi czerpać korzyści z trenowania na zbiorach RAVDESS i nEMO podczas gdy nEMO okazuje się dosyć opornym zbiorem danych do trenowania (ale ciężko znaleźć inny polski zbiór danych)
