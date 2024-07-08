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

