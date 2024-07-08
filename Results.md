# WYNIKI KNN (grid search dla n_neighbours od 1 do 31 i 10 różnych odległości)

## kNN trenowany na zbiorze danych nEMO 
Best parameters found:  {'metric': 'manhattan', 'n_neighbors': 29}

Best cross-validation F1-score:  0.8845100519412388

Test set accuracy (RAVDESS):  0.3333333333333333

Test set F1-score (RAVDESS):  0.25027672085783464

Test set 2 accuracy (nEMO):  0.5264705882352941

Test set 2 F1-score (nEMO):  0.531107924838491


## kNN trenowany na zbiorze danych RAVDESS
Best parameters found:  {'metric': 'manhattan', 'n_neighbors': 1}

Best cross-validation F1-score:  0.8395379741056669

Test set accuracy (RAVDESS):  0.53125

Test set F1-score (RAVDESS):  0.5175705365402405

Test set 2 accuracy (nEMO):  0.2735294117647059

Test set 2 F1-score (nEMO):  0.2061925054112554


## kNN trenowany i testowany na połączeniu zbiorów nEMO i RAVDESS
Best parameters found:  {'metric': 'braycurtis', 'n_neighbors': 5}

Best cross-validation F1-score:  0.8049164716550099

Test set accuracy:  0.4680451127819549

Test set F1-score:  0.46502685390469595



# WYNIKI KNN Z PREPROCESSINGIEM LDA

na podstawie: [link](https://www.researchgate.net/publication/318009355_Cognitive_Gravity_Model_Based_Semi-Supervised_Dimension_Reduction)

[wykres z tego artykułu](https://www.researchgate.net/figure/Accuracies-on-EmoDB-by-using-different-number-of-training-samples-where-KNN-is-utilized_fig5_318009355) 

## trenowany na RAVDESS
Best parameters found:  {'metric': 'chebyshev', 'n_neighbors': 30}
Best cross-validation F1-score:  0.7757445102752729

Test set accuracy (RAVDESS):  0.71875

Test set F1-score (RAVDESS):  0.7149872390848601

Test set 2 accuracy (nEMO):  0.3176470588235294

Test set 2 F1-score (nEMO):  0.2612744429770656

## trenowany na nEMO
est parameters found:  {'metric': 'euclidean', 'n_neighbors': 28}

Best cross-validation F1-score:  0.7814395143023777

Test set accuracy (RAVDESS):  0.328125

Test set F1-score (RAVDESS):  0.2135457279714827   

Test set 2 accuracy (nEMO):  0.4764705882352941

Test set 2 F1-score (nEMO):  0.46302451075369494

## trenowany i testowany na połączeniu zbiorów nEMO i RAVDESS
Best parameters found:  {'metric': 'manhattan', 'n_neighbors': 17}

Best cross-validation F1-score:  0.6354016864628775

Test set accuracy:  0.4567669172932331

Test set F1-score:  0.45626658372264167



# WNIOSKI
1. LDA w połączeniu z kNN daje lepsze wyniki (F1 = 71%) niż sam kNN (F1 = 51%) dla zbioru danych RAVDESS
