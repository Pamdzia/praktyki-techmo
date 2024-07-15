# CLASSIFICATION REPORT DLA NAJLEPSZYCH MODELI

## mini legenda
- klasyfikator_nEMO - model trenowany na zbiorze danych nEMO
- klasyfikator_RAVDESS - model trenowany na zbiorze danych RAVDESS
- klasyfikator_connected - model trenowany na obu (połączonych) zbiorach danych nEMO i RAVDESS

## najlepszy wynik (oba zbiory testowe) dla kNN_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.6429    | 0.9375 | 0.7627   | 48.0    | 0.8542         |
| Happy    | 0.7500    | 0.4375 | 0.5526   | 48.0    | 0.8229         |
| Neutral  | 0.6000    | 0.6875 | 0.6408   | 48.0    | 0.8073         |
| Sad      | 0.4872    | 0.3958 | 0.4368   | 48.0    | 0.7448         |
| **Accuracy**  | **0.6146** | **0.6146** | **0.6146** | **192.0** | **0.6146** |
| **Macro Avg** | **0.6200** | **0.6146** | **0.5982** | **192.0** |                |
| **Weighted Avg** | **0.6200** | **0.6146** | **0.5982** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.2897    | 0.3647 | 0.3229   | 85.0    | 0.6176         |
| Happy    | 0.4756    | 0.4588 | 0.4671   | 85.0    | 0.7382         |
| Neutral  | 0.4545    | 0.4118 | 0.4321   | 85.0    | 0.7294         |
| Sad      | 0.8919    | 0.7765 | 0.8302   | 85.0    | 0.9206         |
| **Accuracy**  | **0.5029** | **0.5029** | **0.5029** | **340.0** | **0.5029** |
| **Macro Avg** | **0.5279** | **0.5029** | **0.5131** | **340.0** |                |
| **Weighted Avg** | **0.5279** | **0.5029** | **0.5131** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla knn_lda_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.7200    | 0.7500 | 0.7347   | 48.0    | 0.8646         |
| Happy    | 0.5128    | 0.4167 | 0.4598   | 48.0    | 0.7552         |
| Neutral  | 0.5179    | 0.6042 | 0.5577   | 48.0    | 0.7604         |
| Sad      | 0.5319    | 0.5208 | 0.5263   | 48.0    | 0.7656         |
| **Accuracy**  | **0.5729** | **0.5729** | **0.5729** | **192.0** | **0.5729** |
| **Macro Avg** | **0.5706** | **0.5729** | **0.5696** | **192.0** |                |
| **Weighted Avg** | **0.5706** | **0.5729** | **0.5696** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.2836    | 0.4471 | 0.3470   | 85.0    | 0.5794         |
| Happy    | 0.3971    | 0.3176 | 0.3529   | 85.0    | 0.7088         |
| Neutral  | 0.5417    | 0.3059 | 0.3910   | 85.0    | 0.7618         |
| Sad      | 0.6111    | 0.6471 | 0.6286   | 85.0    | 0.8088         |
| **Accuracy**  | **0.4294** | **0.4294** | **0.4294** | **340.0** | **0.4294** |
| **Macro Avg** | **0.4584** | **0.4294** | **0.4299** | **340.0** |                |
| **Weighted Avg** | **0.4584** | **0.4294** | **0.4299** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla random_forest_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.6842    | 0.8125 | 0.7429   | 48.0    | 0.8594         |
| Happy    | 0.6400    | 0.3333 | 0.4384   | 48.0    | 0.7865         |
| Neutral  | 0.5306    | 0.5417 | 0.5361   | 48.0    | 0.7656         |
| Sad      | 0.4754    | 0.6042 | 0.5321   | 48.0    | 0.7344         |
| **Accuracy**  | **0.5729** | **0.5729** | **0.5729** | **192.0** | **0.5729** |
| **Macro Avg** | **0.5826** | **0.5729** | **0.5624** | **192.0** |                |
| **Weighted Avg** | **0.5826** | **0.5729** | **0.5624** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.3106    | 0.8588 | 0.4562   | 85.0    | 0.4882         |
| Happy    | 0.6667    | 0.1882 | 0.2936   | 85.0    | 0.7735         |
| Neutral  | 0.4737    | 0.1059 | 0.1731   | 85.0    | 0.7471         |
| Sad      | 0.8387    | 0.6118 | 0.7075   | 85.0    | 0.8735         |
| **Accuracy**  | **0.4412** | **0.4412** | **0.4412** | **340.0** | **0.4412** |
| **Macro Avg** | **0.5724** | **0.4412** | **0.4076** | **340.0** |                |
| **Weighted Avg** | **0.5724** | **0.4412** | **0.4076** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla knn_with_PCA_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.5753    | 0.8750 | 0.6942   | 48.0    | 0.8073         |
| Happy    | 0.5357    | 0.3125 | 0.3947   | 48.0    | 0.7604         |
| Neutral  | 0.5200    | 0.5417 | 0.5306   | 48.0    | 0.7604         |
| Sad      | 0.3902    | 0.3333 | 0.3596   | 48.0    | 0.7031         |
| **Accuracy**  | **0.5156** | **0.5156** | **0.5156** | **192.0** | **0.5156** |
| **Macro Avg** | **0.5053** | **0.5156** | **0.4948** | **192.0** |                |
| **Weighted Avg** | **0.5053** | **0.5156** | **0.4948** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.2195    | 0.3176 | 0.2596   | 85.0    | 0.5471         |
| Happy    | 0.3409    | 0.3529 | 0.3468   | 85.0    | 0.6676         |
| Neutral  | 0.4262    | 0.3059 | 0.3562   | 85.0    | 0.7235         |
| Sad      | 0.8971    | 0.7176 | 0.7974   | 85.0    | 0.9088         |
| **Accuracy**  | **0.4235** | **0.4235** | **0.4235** | **340.0** | **0.4235** |
| **Macro Avg** | **0.4709** | **0.4235** | **0.4400** | **340.0** |                |
| **Weighted Avg** | **0.4709** | **0.4235** | **0.4400** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla SVC_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.7213    | 0.9167 | 0.8073   | 48.0    | 0.8906         |
| Happy    | 0.6154    | 0.5000 | 0.5517   | 48.0    | 0.7969         |
| Neutral  | 0.7647    | 0.5417 | 0.6341   | 48.0    | 0.8438         |
| Sad      | 0.5172    | 0.6250 | 0.5660   | 48.0    | 0.7604         |
| **Accuracy**  | **0.6458** | **0.6458** | **0.6458** | **192.0** | **0.6458** |
| **Macro Avg** | **0.6547** | **0.6458** | **0.6398** | **192.0** |                |
| **Weighted Avg** | **0.6547** | **0.6458** | **0.6398** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.3364    | 0.8588 | 0.4834   | 85.0    | 0.5412         |
| Happy    | 0.3571    | 0.1176 | 0.1770   | 85.0    | 0.7265         |
| Neutral  | 0.3611    | 0.3059 | 0.3312   | 85.0    | 0.6912         |
| Sad      | 1.0000    | 0.2706 | 0.4259   | 85.0    | 0.8176         |
| **Accuracy**  | **0.3882** | **0.3882** | **0.3882** | **340.0** | **0.3882** |
| **Macro Avg** | **0.5137** | **0.3882** | **0.3544** | **340.0** |                |
| **Weighted Avg** | **0.5137** | **0.3882** | **0.3544** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla SVC_with_LDA_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.7273    | 0.6667 | 0.6957   | 48.0    | 0.8542         |
| Happy    | 0.5238    | 0.4583 | 0.4889   | 48.0    | 0.7604         |
| Neutral  | 0.5345    | 0.6458 | 0.5849   | 48.0    | 0.7708         |
| Sad      | 0.5208    | 0.5208 | 0.5208   | 48.0    | 0.7604         |
| **Accuracy**  | **0.5729** | **0.5729** | **0.5729** | **192.0** | **0.5729** |
| **Macro Avg** | **0.5766** | **0.5729** | **0.5726** | **192.0** |                |
| **Weighted Avg** | **0.5766** | **0.5729** | **0.5726** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.2982    | 0.4000 | 0.3417   | 85.0    | 0.6147         |
| Happy    | 0.4487    | 0.4118 | 0.4294   | 85.0    | 0.7265         |
| Neutral  | 0.5172    | 0.3529 | 0.4196   | 85.0    | 0.7559         |
| Sad      | 0.6000    | 0.6353 | 0.6171   | 85.0    | 0.8029         |
| **Accuracy**  | **0.4500** | **0.4500** | **0.4500** | **340.0** | **0.4500** |
| **Macro Avg** | **0.4661** | **0.4500** | **0.4520** | **340.0** |                |
| **Weighted Avg** | **0.4661** | **0.4500** | **0.4520** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla SVC_with_PCA_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.6774    | 0.8750 | 0.7636   | 48.0    | 0.8646         |
| Happy    | 0.6286    | 0.4583 | 0.5301   | 48.0    | 0.7969         |
| Neutral  | 0.7143    | 0.6250 | 0.6667   | 48.0    | 0.8438         |
| Sad      | 0.4906    | 0.5417 | 0.5149   | 48.0    | 0.7448         |
| **Accuracy**  | **0.6250** | **0.6250** | **0.6250** | **192.0** | **0.6250** |
| **Macro Avg** | **0.6277** | **0.6250** | **0.6188** | **192.0** |                |
| **Weighted Avg** | **0.6277** | **0.6250** | **0.6188** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.3467    | 0.8118 | 0.4859   | 85.0    | 0.5706         |
| Happy    | 0.4884    | 0.2471 | 0.3281   | 85.0    | 0.7471         |
| Neutral  | 0.4872    | 0.2235 | 0.3065   | 85.0    | 0.7471         |
| Sad      | 0.9492    | 0.6588 | 0.7778   | 85.0    | 0.9059         |
| **Accuracy**  | **0.4853** | **0.4853** | **0.4853** | **340.0** | **0.4853** |
| **Macro Avg** | **0.5679** | **0.4853** | **0.4746** | **340.0** |                |
| **Weighted Avg** | **0.5679** | **0.4853** | **0.4746** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla MLP_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.7679    | 0.8958 | 0.8269   | 48.0    | 0.9063         |
| Happy    | 0.5870    | 0.5625 | 0.5745   | 48.0    | 0.7917         |
| Neutral  | 0.7632    | 0.6042 | 0.6744   | 48.0    | 0.8542         |
| Sad      | 0.5385    | 0.5833 | 0.5600   | 48.0    | 0.7708         |
| **Accuracy**  | **0.6615** | **0.6615** | **0.6615** | **192.0** | **0.6615** |
| **Macro Avg** | **0.6641** | **0.6615** | **0.6590** | **192.0** |                |
| **Weighted Avg** | **0.6641** | **0.6615** | **0.6590** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.3804    | 0.7294 | 0.5000   | 85.0    | 0.6353         |
| Happy    | 0.4590    | 0.3294 | 0.3836   | 85.0    | 0.7353         |
| Neutral  | 0.4286    | 0.3529 | 0.3871   | 85.0    | 0.7206         |
| Sad      | 0.8478    | 0.4588 | 0.5954   | 85.0    | 0.8441         |
| **Accuracy**  | **0.4676** | **0.4676** | **0.4676** | **340.0** | **0.4676** |
| **Macro Avg** | **0.5289** | **0.4676** | **0.4665** | **340.0** |                |
| **Weighted Avg** | **0.5289** | **0.4676** | **0.4665** | **340.0** |                |


## najlepszy wynik (oba zbiory testowe) dla MLP_from_git_updated_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.5541    | 0.8542 | 0.6721   | 48.0    | 0.7917         |
| Happy    | 0.3214    | 0.1875 | 0.2368   | 48.0    | 0.6979         |
| Neutral  | 0.6094    | 0.8125 | 0.6964   | 48.0    | 0.8229         |
| Sad      | 0.8077    | 0.4375 | 0.5676   | 48.0    | 0.8333         |
| **Accuracy**  | **0.5729** | **0.5729** | **0.5729** | **192.0** | **0.5729** |
| **Macro Avg** | **0.5731** | **0.5729** | **0.5432** | **192.0** |                |
| **Weighted Avg** | **0.5731** | **0.5729** | **0.5432** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.3409    | 0.3529 | 0.3468   | 85.0    | 0.6676         |
| Happy    | 0.3854    | 0.4353 | 0.4088   | 85.0    | 0.6853         |
| Neutral  | 0.5075    | 0.4000 | 0.4474   | 85.0    | 0.7529         |
| Sad      | 0.6854    | 0.7176 | 0.7011   | 85.0    | 0.8471         |
| **Accuracy**  | **0.4765** | **0.4765** | **0.4765** | **340.0** | **0.4765** |
| **Macro Avg** | **0.4798** | **0.4765** | **0.4760** | **340.0** |                |
| **Weighted Avg** | **0.4798** | **0.4765** | **0.4760** | **340.0** |                |

## najlepszy wynik (oba zbiory testowe) dla MLP_from_git_updated2_connected
### classification report dla zbioru danych RAVDESS
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.6056    | 0.8958 | 0.7227   | 48.0    | 0.8281         |
| Happy    | 0.5200    | 0.2708 | 0.3562   | 48.0    | 0.7552         |
| Neutral  | 0.6071    | 0.7083 | 0.6538   | 48.0    | 0.8125         |
| Sad      | 0.6000    | 0.5000 | 0.5455   | 48.0    | 0.7917         |
| **Accuracy**  | **0.5938** | **0.5938** | **0.5938** | **192.0** | **0.5938** |
| **Macro Avg** | **0.5832** | **0.5938** | **0.5695** | **192.0** |                |
| **Weighted Avg** | **0.5832** | **0.5938** | **0.5695** | **192.0** |                |

### classification report dla zbioru danych nEMO
| Emotion  | Precision | Recall | F1-Score | Support | Class Accuracy |
|----------|-----------|--------|----------|---------|----------------|
| Angry    | 0.4639    | 0.5294 | 0.4945   | 85.0    | 0.7294         |
| Happy    | 0.4603    | 0.6824 | 0.5498   | 85.0    | 0.7206         |
| Neutral  | 0.4138    | 0.4235 | 0.4186   | 85.0    | 0.7059         |
| Sad      | 0.8667    | 0.3059 | 0.4522   | 85.0    | 0.8147         |
| **Accuracy**  | **0.4853** | **0.4853** | **0.4853** | **340.0** | **0.4853** |
| **Macro Avg** | **0.5512** | **0.4853** | **0.4788** | **340.0** |                |
| **Weighted Avg** | **0.5512** | **0.4853** | **0.4788** | **340.0** |                |
