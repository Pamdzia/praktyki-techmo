# PORÓWNANIE F1 DLA WSZYSTKICH DOTYCHCZAS UZYTYCH MODELI

## mini legenda
- klasyfikator_nEMO - model trenowany na zbiorze danych nEMO
- klasyfikator_RAVDESS - model trenowany na zbiorze danych RAVDESS
- klasyfikator_connected - model trenowany na obu (połączonych) zbiorach danych nEMO i RAVDESS
- klasyfikator_iemocap_connected - model treniwany na zbiorze danych IEMOCAP połączonych (gra aktorska i improwizacja)
- klasyfikator_iemocap_impro - model treniwany na zbiorze danych IEMOCAP improwizacyjnych
- klasyfikator_iemocap_script - model treniwany na zbiorze danych IEMOCAP skryptowych
- klasyfikator_emo_db - model treniwany na zbiorze danych emoDB (język niemicki)

## tabelka
| F1-Score | Experiment Name                 |
|----------|---------------------------------|
| 0.6557   | SVC_RAVDESS                     |
| 0.1      | SVC_RAVDESS                     |
| 0.6398   | SVC_connected                   |
| 0.3544   | SVC_connected                   |
| 0.1399   | SVC_nEMO                        |
| 0.3201   | SVC_nEMO                        |
| 0.5360   | knn_RAVDESS                     |
| 0.0991   | knn_RAVDESS                     |
| 0.5982   | knn_connected                   |
| 0.5131   | knn_connected                   |
| 0.2204   | knn_emo_db                      |
| 0.3547   | knn_emo_db                      |
| 0.2371   | knn_iemocap_connected           |
| 0.1991   | knn_iemocap_connected           |
| 0.2737   | knn_iemocap_impro               |
| 0.1149   | knn_iemocap_impro               |
| 0.1997   | knn_iemocap_script              |
| 0.3121   | knn_iemocap_script              |
| 0.6894   | knn_lda_RAVDESS                 |
| 0.2294   | knn_lda_RAVDESS                 |
| 0.5696   | knn_lda_connected               |
| 0.4299   | knn_lda_connected               |
| 0.2664   | knn_lda_emo_db                  |
| 0.2398   | knn_lda_emo_db                  |
| 0.1952   | knn_lda_iemocap_connected       |
| 0.1010   | knn_lda_iemocap_connected       |
| 0.2222   | knn_lda_iemocap_impro           |
| 0.1002   | knn_lda_iemocap_impro           |
| 0.1066   | knn_lda_iemocap_script          |
| 0.1283   | knn_lda_iemocap_script          |
| 0.2135   | knn_lda_nEMO                    |
| 0.4630   | knn_lda_nEMO                    |
| 0.2503   | knn_nEMO                        |
| 0.5311   | knn_nEMO                        |
| 0.5362   | knn_with_PCA_RAVDESS            |
| 0.1005   | knn_with_PCA_RAVDESS            |
| 0.4948   | knn_with_PCA_connected          |
| 0.4400   | knn_with_PCA_connected          |
| 0.2673   | knn_with_PCA_nEMO               |
| 0.5205   | knn_with_PCA_nEMO               |
| 0.6755   | mlp_RAVDESS                     |
| 0.1956   | mlp_RAVDESS                     |
| 0.6590   | mlp_combined                    |
| 0.4665   | mlp_combined                    |
| 0.1249   | mlp_nEMO                        |
| 0.4305   | mlp_nEMO                        |
| 0.5505   | random_forest_RAVDESS           |
| 0.1709   | random_forest_RAVDESS           |
| 0.5624   | random_forest_connected         |
| 0.4076   | random_forest_connected         |
| 0.2825   | random_forest_emo_db            |
| 0.3222   | random_forest_emo_db            |
| 0.2874   | random_forest_iemocap_connected |
| 0.1      | random_forest_iemocap_connected |
| 0.2957   | random_forest_iemocap_impro     |
| 0.1      | random_forest_iemocap_impro     |
| 0.3005   | random_forest_iemocap_script    |
| 0.1007   | random_forest_iemocap_script    |
| 0.3717   | random_forest_nEMO              |
| 0.3866   | random_forest_nEMO              |
