# PORÓWNANIE F1 DLA WSZYSTKICH DOTYCHCZAS UZYTYCH MODELI

## mini legenda
- klasyfikator_nEMO - model trenowany na zbiorze danych nEMO
- klasyfikator_RAVDESS - model trenowany na zbiorze danych RAVDESS
- klasyfikator_connected - model trenowany na obu (połączonych) zbiorach danych nEMO i RAVDESS
- klasyfikator_iemocap_connected - model treniwany na zbiorze danych IEMOCAP połączonych (gra aktorska i improwizacja)
- klasyfikator_iemocap_impro - model treniwany na zbiorze danych IEMOCAP improwizacyjnych
- klasyfikator_iemocap_script - model treniwany na zbiorze danych IEMOCAP skryptowych
- klasyfikator_emo_db - model treniwany na zbiorze danych emoDB (język niemicki)
- MLP_from_git_updated - model Sequential z warstwami Dense i Dropout
- MLP_from_git_updated2 - model Sequential z warstwami Dense, Dropout i BatchNormalization
  
## tabelka
| F1-Score | Experiment Name                    | Dataset Name |
|----------|------------------------------------|--------------|
| 0.7232   | MLP_from_git_updated2_RAVDESS      | RAVDESS      |
| 0.1241   | MLP_from_git_updated2_RAVDESS      | nEMO         |
| 0.5695   | MLP_from_git_updated2_connected    | RAVDESS      |
| 0.4788   | MLP_from_git_updated2_connected    | nEMO         |
| 0.1641   | MLP_from_git_updated2_nEMO         | RAVDESS      |
| 0.4195   | MLP_from_git_updated2_nEMO         | nEMO         |
| 0.7073   | MLP_from_git_updated_RAVDESS       | RAVDESS      |
| 0.1298   | MLP_from_git_updated_RAVDESS       | nEMO         |
| 0.5432   | MLP_from_git_updated_connected     | RAVDESS      |
| 0.4760   | MLP_from_git_updated_connected     | nEMO         |
| 0.1000   | MLP_from_git_updated_nEMO          | RAVDESS      |
| 0.4416   | MLP_from_git_updated_nEMO          | nEMO         |
| 0.6557   | SVC_RAVDESS                        | RAVDESS      |
| 0.1000   | SVC_RAVDESS                        | nEMO         |
| 0.6398   | SVC_connected                      | RAVDESS      |
| 0.3544   | SVC_connected                      | nEMO         |
| 0.6503   | SVC_linear_RAVDESS                 | RAVDESS      |
| 0.1000   | SVC_linear_RAVDESS                 | nEMO         |
| 0.6398   | SVC_linear_connected               | RAVDESS      |
| 0.3544   | SVC_linear_connected               | nEMO         |
| 0.1399   | SVC_linear_nEMO                    | RAVDESS      |
| 0.3201   | SVC_linear_nEMO                    | nEMO         |
| 0.1399   | SVC_nEMO                           | RAVDESS      |
| 0.3201   | SVC_nEMO                           | nEMO         |
| 0.7047   | SVC_with_LDA_RAVDESS               | RAVDESS      |
| 0.2265   | SVC_with_LDA_RAVDESS               | nEMO         |
| 0.5726   | SVC_with_LDA_connected             | RAVDESS      |
| 0.4520   | SVC_with_LDA_connected             | nEMO         |
| 0.2084   | SVC_with_LDA_nEMO                  | RAVDESS      |
| 0.4638   | SVC_with_LDA_nEMO                  | nEMO         |
| 0.5830   | SVC_with_PCA_RAVDESS               | RAVDESS      |
| 0.1000   | SVC_with_PCA_RAVDESS               | nEMO         |
| 0.6188   | SVC_with_PCA_connected             | RAVDESS      |
| 0.4746   | SVC_with_PCA_connected             | nEMO         |
| 0.1674   | SVC_with_PCA_nEMO                  | RAVDESS      |
| 0.3738   | SVC_with_PCA_nEMO                  | nEMO         |
| 0.5360   | knn_RAVDESS                        | RAVDESS      |
| 0.0991   | knn_RAVDESS                        | nEMO         |
| 0.5982   | knn_connected                      | RAVDESS      |
| 0.5131   | knn_connected                      | nEMO         |
| 0.2204   | knn_emo_db                         | RAVDESS      |
| 0.3547   | knn_emo_db                         | nEMO         |
| 0.2371   | knn_iemocap_connected              | RAVDESS      |
| 0.1991   | knn_iemocap_connected              | nEMO         |
| 0.2737   | knn_iemocap_impro                  | RAVDESS      |
| 0.1149   | knn_iemocap_impro                  | nEMO         |
| 0.1997   | knn_iemocap_script                 | RAVDESS      |
| 0.3121   | knn_iemocap_script                 | nEMO         |
| 0.6894   | knn_lda_RAVDESS                    | RAVDESS      |
| 0.2294   | knn_lda_RAVDESS                    | nEMO         |
| 0.5696   | knn_lda_connected                  | RAVDESS      |
| 0.4299   | knn_lda_connected                  | nEMO         |
| 0.2664   | knn_lda_emo_db                     | RAVDESS      |
| 0.2398   | knn_lda_emo_db                     | nEMO         |
| 0.1952   | knn_lda_iemocap_connected          | RAVDESS      |
| 0.1010   | knn_lda_iemocap_connected          | nEMO         |
| 0.2222   | knn_lda_iemocap_impro              | RAVDESS      |
| 0.1002   | knn_lda_iemocap_impro              | nEMO         |
| 0.1066   | knn_lda_iemocap_script             | RAVDESS      |
| 0.1283   | knn_lda_iemocap_script             | nEMO         |
| 0.2135   | knn_lda_nEMO                       | RAVDESS      |
| 0.4630   | knn_lda_nEMO                       | nEMO         |
| 0.2503   | knn_nEMO                           | RAVDESS      |
| 0.5311   | knn_nEMO                           | nEMO         |
| 0.5362   | knn_with_PCA_RAVDESS               | RAVDESS      |
| 0.1005   | knn_with_PCA_RAVDESS               | nEMO         |
| 0.4948   | knn_with_PCA_connected             | RAVDESS      |
| 0.4400   | knn_with_PCA_connected             | nEMO         |
| 0.2673   | knn_with_PCA_nEMO                  | RAVDESS      |
| 0.5205   | knn_with_PCA_nEMO                  | nEMO         |
| 0.6755   | mlp_RAVDESS                        | RAVDESS      |
| 0.1956   | mlp_RAVDESS                        | nEMO         |
| 0.6590   | mlp_combined                       | RAVDESS      |
| 0.4665   | mlp_combined                       | nEMO         |
| 0.1249   | mlp_nEMO                           | RAVDESS      |
| 0.4305   | mlp_nEMO                           | nEMO         |
| 0.5505   | random_forest_RAVDESS              | RAVDESS      |
| 0.1709   | random_forest_RAVDESS              | nEMO         |
| 0.5624   | random_forest_connected            | RAVDESS      |
| 0.4076   | random_forest_connected            | nEMO         |
| 0.2825   | random_forest_emo_db               | RAVDESS      |
| 0.3222   | random_forest_emo_db               | nEMO         |
| 0.2874   | random_forest_iemocap_connected    | RAVDESS      |
| 0.1000   | random_forest_iemocap_connected    | nEMO         |
| 0.2957   | random_forest_iemocap_impro        | RAVDESS      |
| 0.1000   | random_forest_iemocap_impro        | nEMO         |
| 0.3005   | random_forest_iemocap_script       | RAVDESS      |
| 0.1007   | random_forest_iemocap_script       | nEMO         |
| 0.3717   | random_forest_nEMO                 | RAVDESS      |
| 0.3866   | random_forest_nEMO                 | nEMO         |
