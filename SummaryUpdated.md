**nEMO** - język polski
**RAVDESS** - język angielski
**emoDB** - język niemiecki
**TESS** - język angielski

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

## pełne wyniki
[wyniki precyzji dla modeli testowanych na zbiorze danych nEMO i trenowanych na RAVDESS/nEMO/RAVDESS+nEMO](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/precision_results_nEMO.txt)

[wyniki precyzji dla modeli testowanych na zbiorze danych nEMO i trenowanych na emoDB](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/precision_results_emo_DB_nEMO.txt)

[wyniki precyzji dla modeli testowanych na zbiorze danych RAVDESS i trenowanych na RAVDESS/nEMO/RAVDESS+nEMO](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/precision_results_RAVDESS.txt)

[wyniki precyzji dla modeli testowanych na zbiorze danych RAVDESS i trenowanych na emoDB](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/precision_results_emo_DB_RAVDESS.txt)

[wyniki precyzji dla modeli testowanych na zbiorze danych RAVDESS i trenowanych na TESS](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/precision_results_TESS_RAVESS.txt)

[wyniki precyzji dla modeli testowanych na zbiorze danych nEMO i trenowanych na TESS](https://github.com/Pamdzia/praktyki-techmo/blob/main/data-testing/precision_results_TESS_nEMO.txt)

## Testowanie na nEMO modeli trenowanych na RAVDESS
- Większość modeli miała trudności z rozpoznawaniem emocji z precyzją powyżej 0.5. Żadna emocja nie osiągnęła precyzji powyżej 0.5 w żadnym z eksperymentów. Najlepiej rozpoznawane emocje to zazwyczaj "happy" (szczęśliwy) lub "sad" (smutny).

- "Happy" uzyskało najwyższą precyzję w kilku eksperymentach: MLP_from_git_updated2_RAVDESS (0.24), SVC_RAVDESS (0.25), SVC_linear_RAVDESS (0.25), SVC_with_PCA_RAVDESS (0.25), knn_RAVDESS (0.25), knn_with_PCA_RAVDESS (0.25). Jednak w żadnym z nich nie przekroczyło 0.5.

- "Sad" uzyskało nieco wyższą precyzję w niektórych eksperymentach: MLP_from_git_updated_RAVDESS (0.26), SVC_with_LDA_RAVDESS (0.4), knn_lda_RAVDESS (0.4), mlp_RAVDESS (0.41).

- "Angry" (zły), "neutral" (neutralny) i "sad" często miały precyzję poniżej 0.2 w wielu eksperymentach:

- "Angry": MLP_from_git_updated_RAVDESS (0.0), SVC_RAVDESS (0.0), SVC_linear_RAVDESS (0.0), SVC_with_LDA_RAVDESS (0.0), SVC_with_PCA_RAVDESS (0.0), knn_RAVDESS (0.0), knn_lda_RAVDESS (0.0), knn_with_PCA_RAVDESS (0.0), random_forest_RAVDESS (0.28).
- "Neutral": MLP_from_git_updated2_RAVDESS (0.02), MLP_from_git_updated_RAVDESS (0.03), SVC_RAVDESS (0.0), SVC_linear_RAVDESS (0.0), SVC_with_PCA_RAVDESS (0.0), knn_RAVDESS (0.0), knn_with_PCA_RAVDESS (0.0), mlp_RAVDESS (0.0), random_forest_RAVDESS (0.0).
- "Sad": MLP_from_git_updated2_RAVDESS (0.17), SVC_RAVDESS (0.0), SVC_linear_RAVDESS (0.0), SVC_with_PCA_RAVDESS (0.0), knn_RAVDESS (0.0), knn_with_PCA_RAVDESS (0.0), random_forest_RAVDESS (0.0).
"Angry" i "neutral" były często rozpoznawane z precyzją równą 0.0, co oznacza całkowite niepowodzenie w ich identyfikacji:

- "Angry": MLP_from_git_updated_RAVDESS, SVC_RAVDESS, SVC_linear_RAVDESS, SVC_with_LDA_RAVDESS, SVC_with_PCA_RAVDESS, knn_RAVDESS, knn_lda_RAVDESS, knn_with_PCA_RAVDESS.
- "Neutral": SVC_RAVDESS, SVC_linear_RAVDESS, SVC_with_PCA_RAVDESS, knn_RAVDESS, knn_with_PCA_RAVDESS, mlp_RAVDESS, random_forest_RAVDESS.


## Testowanie na nEMO modeli trenowanych na nEMO
- Emocją, która jest najlepiej rozpoznawana w prawie wszystkich eksperymentach, jest "sad" (smutny). Precyzja w rozpoznawaniu tej emocji jest bardzo wysoka, często osiągając wartości bliskie 1.0 (100%). Osiągnięto ją w eksperymentach: MLP_from_git_updated2_nEMO (0.89), MLP_from_git_updated_nEMO (0.89), SVC_linear_nEMO (1.0), SVC_nEMO (1.0), SVC_with_LDA_nEMO (0.86), SVC_with_PCA_nEMO (0.96), knn_lda_nEMO (0.84), knn_nEMO (0.91), knn_with_PCA_nEMO (0.9), mlp_nEMO (0.91), random_forest_nEMO (0.88).
  
- W zdecydowanej większości eksperymentów jedyną emocją, która osiągnęła precyzję powyżej 0.5, jest "sad". Osiągnięto ją w eksperymentach: MLP_from_git_updated2_nEMO, MLP_from_git_updated_nEMO, SVC_linear_nEMO, SVC_nEMO, SVC_with_LDA_nEMO, SVC_with_PCA_nEMO, knn_lda_nEMO, knn_nEMO, knn_with_PCA_nEMO, mlp_nEMO, random_forest_nEMO.

- Większość emocji rozpoznawana jest na poziomie powyżej 0.2, ale poniżej 0.5, z dwoma wyjątkami „happy”:
"Happy" osiągnęło precyzję powyżej 0.2, ale poniżej 0.5, w eksperymentach: knn_nEMO (powyżej 0.5), mlp_nEMO (powyżej 0.5), SVC_linear_nEMO (0.12), SVC_nEMO (0.12).


## Testowanie na nEMO modeli trenowanych na RAVDESS i nEMO
- Emocja "sad" (smutny) jest najlepiej rozpoznawana w większości eksperymentów. Precyzja rozpoznawania tej emocji jest bardzo wysoka, często osiągając wartości bliskie 1.0 (100%). Osiągnięto ją w eksperymentach: MLP_from_git_updated2_connected (0.87), MLP_from_git_updated_connected (0.69), SVC_connected (1.0), SVC_linear_connected (1.0), SVC_with_LDA_connected (0.6), SVC_with_PCA_connected (0.95), knn_connected (0.89), knn_lda_connected (0.61), knn_with_PCA_connected (0.9), mlp_combined (0.85), random_forest_connected (0.84).

- Modele radzą sobie również dobrze z rozpoznawaniem emocji "neutral". Osiągnięto ją w eksperymentach: MLP_from_git_updated_connected (precyzja: 0.69), SVC_with_LDA_connected (precyzja: 0.6), knn_lda_connected (precyzja: 0.61).

## Testowanie na RAVDESS modeli trenowanych na nEMO
- Emocja "sad" (smutny) jest najlepiej rozpoznawana w wielu eksperymentach, osiągając precyzję zazwyczaj powyżej lub równą 0.5. Osiągnięto ją w eksperymentach: MLP_from_git_updated2_nEMO (1.0), SVC_linear_nEMO (0.8), SVC_nEMO (0.8), SVC_with_PCA_nEMO (0.5), mlp_nEMO (1.0).
Emocje "happy" (szczęśliwy) i "neutral" (neutralny) mają precyzję poniżej 0.2 w wielu eksperymentach:

- "Happy" osiągnęło precyzję poniżej 0.2 w eksperymentach: MLP_from_git_updated_nEMO (0.0), SVC_linear_nEMO (0.0), SVC_nEMO (0.0), SVC_with_LDA_nEMO (0.0), SVC_with_PCA_nEMO (0.0), knn_lda_nEMO (0.0), mlp_nEMO (0.07).

- "Neutral" osiągnęło precyzję poniżej 0.2 w eksperymentach: MLP_from_git_updated2_nEMO (0.0), MLP_from_git_updated_nEMO (0.0), SVC_linear_nEMO (0.0), SVC_nEMO (0.0), SVC_with_LDA_nEMO (0.0), SVC_with_PCA_nEMO (0.0), knn_lda_nEMO (0.0), knn_nEMO (0.0), knn_with_PCA_nEMO (0.0), mlp_nEMO (0.0), random_forest_nEMO (0.0).

- Precyzja rozpoznawania emocji "neutral" wynosi 0.0 w większości eksperymentów: MLP_from_git_updated2_nEMO, MLP_from_git_updated_nEMO, SVC_linear_nEMO, SVC_nEMO, SVC_with_LDA_nEMO, SVC_with_PCA_nEMO, knn_lda_nEMO, knn_nEMO, knn_with_PCA_nEMO, mlp_nEMO, random_forest_nEMO.

- Emocja "happy" osiągnęła precyzję 0.0 w wielu eksperymentach: MLP_from_git_updated_nEMO, SVC_linear_nEMO, SVC_nEMO, SVC_with_LDA_nEMO, SVC_with_PCA_nEMO, knn_lda_nEMO.

## Testowanie na RAVDESS modeli trenowanych na RAVDESS
- Zbiór danych RAVDESS oraz zastosowane modele są skuteczne w rozpoznawaniu różnych emocji, osiągając precyzję powyżej 0.5 dla wszystkich emocji w większości eksperymentów.

- Najwyższą precyzję zazwyczaj mają emocje "angry" (zły) i "neutral" (neutralny). Osiągnięto ją w eksperymentach:
MLP_from_git_updated2_RAVDESS: angry (0.84)
MLP_from_git_updated_RAVDESS: neutral (0.78)
SVC_RAVDESS: neutral (0.73)
SVC_linear_RAVDESS: neutral (0.72)
SVC_with_LDA_RAVDESS: neutral (0.78)
SVC_with_PCA_RAVDESS: angry (0.65)
knn_RAVDESS: neutral (0.65)
knn_lda_RAVDESS: neutral (0.74)
knn_with_PCA_RAVDESS: happy (0.62)
mlp_RAVDESS: neutral (0.76)
random_forest_RAVDESS: angry (0.68)

- Żaden z modeli nie ma trudności z rozpoznawaniem emocji poniżej precyzji 0.2.

## Testowanie na RAVDESS modeli trenowanych na nEMO i RAVDESS
- Wszystkie emocje ("angry", "happy", "neutral", "sad") osiągnęły precyzję powyżej 0.5 w większości eksperymentów:
MLP_from_git_updated2_connected: angry (0.61), happy (0.59), neutral (0.61), sad (0.58)
MLP_from_git_updated_connected: angry (0.70), neutral (0.81), sad (0.81)
SVC_connected: angry (0.74), happy (0.72), neutral (0.76), sad (0.73)
SVC_linear_connected: angry (0.74), happy (0.72), neutral (0.76), sad (0.73)
SVC_with_LDA_connected: angry (0.73), happy (0.71), neutral (0.75), sad (0.74)
SVC_with_PCA_connected: angry (0.71), happy (0.72), neutral (0.71)
knn_connected: angry (0.70), happy (0.75), neutral (0.71)
knn_lda_connected: angry (0.72), happy (0.73), neutral (0.74), sad (0.72)
knn_with_PCA_connected: angry (0.58), happy (0.60), neutral (0.61)
mlp_combined: angry (0.77), happy (0.76), neutral (0.78), sad (0.75)
random_forest_connected: angry (0.68), happy (0.66), neutral (0.67)

- W żadnym z eksperymentów nie ma emocji z precyzją poniżej 0.2.

## Testowanie na nEMO modeli trenowanych na emoDB
- Emocja "sad" (smutny) jest najlepiej rozpoznawana w większości eksperymentów. W wielu przypadkach osiąga precyzję 1.0 (100%), co oznacza, że modele bardzo skutecznie identyfikują tę emocję.

- Eksperymenty z precyzją 1.0 dla emocji "sad":
MLP_from_git_updated2_emo_DB
MLP_from_git_updated_emo_DB
SVC_emo_DB
SVC_with_PCA_emo_DB
mlp_emo_DB

- Emocja "neutral" (neutralny) również jest dobrze rozpoznawana w niektórych eksperymentach, chociaż nie osiąga tak wysokiej precyzji jak "sad".

- Najlepiej rozpoznana emocja "neutral" w eksperymentach:
SVC_with_LDA_emo_DB (0.39)
knn_lda_emoDB (0.38)

- Emocje "angry" (zły) i "happy" (szczęśliwy) mają trudności z osiągnięciem wysokiej precyzji i często są rozpoznawane z precyzją poniżej 0.2 w wielu eksperymentach.

- Eksperymenty z precyzją poniżej 0.2 dla emocji "angry":
MLP_from_git_updated2_emo_DB (0.15)
SVC_emo_DB (0.19)
SVC_with_PCA_emo_DB (0.15)

- Eksperymenty z precyzją poniżej 0.2 dla emocji "happy":
MLP_from_git_updated_emo_DB (0.18)
SVC_emo_DB (0.18)
SVC_with_LDA_emo_DB (0.1)
knn_lda_emoDB (0.05)
knn_with_PCA_emo_DB (0.19)
mlp_emo_DB (0.12)

## Testowanie na RAVDESS modeli trenowanych na emoDB
- Emocja "angry" (zły) jest najlepiej rozpoznawana w większości eksperymentów, często osiągając precyzję powyżej 0.5. Modele radzą sobie najlepiej z identyfikacją tej emocji.
  
- Eksperymenty z precyzją powyżej 0.5 dla emocji "angry":
MLP_from_git_updated2_emo_DB (0.54)
MLP_from_git_updated_emo_DB (0.6)
SVC_with_LDA_emo_DB (0.57)
mlp_emo_DB (0.77)
random_forest_emo_db (0.65)

- Emocje "happy" (szczęśliwy) i "sad" (smutny) są najtrudniejsze do rozpoznania przez modele, często uzyskując precyzję poniżej 0.2 w wielu eksperymentach.

- Eksperymenty z precyzją poniżej 0.2 dla emocji "happy":
MLP_from_git_updated2_emo_DB (0.17)
MLP_from_git_updated_emo_DB (0.13)
SVC_emo_DB (0.12)
SVC_with_LDA_emo_DB (0.18)
SVC_with_PCA_emo_DB (0.18)
knn_emo_db (0.07)
knn_lda_emoDB (0.19)
knn_with_PCA_emo_DB (0.18)

- Eksperymenty z precyzją poniżej 0.2 dla emocji "sad":
MLP_from_git_updated_emo_DB (0.0)
SVC_emo_DB (0.0)
SVC_with_PCA_emo_DB (0.0)
knn_emo_db (0.16)
mlp_emo_DB (0.0)
random_forest_emo_db (0.14)
knn_with_PCA_emo_DB (0.14)

- Emocja "neutral" (neutralny) jest również trudna do rozpoznania przez niektóre modele, uzyskując precyzję poniżej 0.2 w kilku eksperymentach.

- Eksperymenty z precyzją poniżej 0.2 dla emocji "neutral":
SVC_with_LDA_emo_DB (0.17)
knn_lda_emoDB (0.15)
mlp_emo_DB (0.19)

- Podsumowując, modele najlepiej radzą sobie z rozpoznawaniem emocji "angry", natomiast emocje "happy" i "sad" są najtrudniejsze do rozpoznania. Modele SVC_with_PCA oraz niektóre wersje kNN mają najwięcej trudności z dokładniejszym rozpoznaniem jakiejkowliek emozcji.

## Testowanie na RAVDESS modeli trenowanych na TESS
- w pięciu na osiem (SVC_tess, SVC_with_LDA_tess, SVC_with_PCA_tess, knn_lda_tess, knn_tess, knn_with_PCA_tess, mlp_tess, random_forest_tess) eksperymentów trenownaych na zbiorze danych TESS najwyższą precyzję uzyskała emocja "sad":
SVC_tess (0.67)
SVC_with_LDA_tess (0.52)
SVC_with_PCA_tess (1.0)
mlp_tess (0.8)
random_forest_tess (0.75)

- w eksperymentach z knn największą precyzję uzyskano dla emocji "neutral" i "angry":
knn_lda_tess (angry: 0.5)
knn_tess (neutral: 0.4)
knn_with_PCA_tess (neutral: 0.55)

- żadna emocja oprócz "happy" nie spadła w precyzji poniżej 0.2

- eksperymenty z precyzją dla happy poniżej 0.2:
SVC_tess (0.12)
SVC_with_LDA_tess (0.18)
SVC_with_PCA_tess (0.0)
knn_with_PCA_tess (0.07)
mlp_tess (0.14)

- precyzja powyżej 0.5 dla emcoji "neutral" występowała także dla modeli:
mlp_tess
SVC_tess

## Testowanie na nEMO modeli trenowanych na TESS
- we wszystkich ośmiu eksperymentach (takich samych jak powyżej) najlepsze wyniki uzyskano dla emocji "sad":
SVC_tess (0.76)
SVC_with_LDA_tess (0.9)
SVC_with_PCA_tess (0.78)
knn_lda_tess (0.75)
knn_tess (0.55)
knn_with_PCA_tess (0.6)
mlp_tess (0.87)
random_forest_tess (0.84)

- najlepsze wyniki uzyskano dla modeli SVC_with_LDA_tess i knn_lda_tess (oba modele z LDA !) gdize wszystkie emocje osiągnęy precyzje powyżej 0.5

- w sześciu pozostałych eksperymentach emocja "angry" osiągnęła precyzję poniżej 0.2

# WNIOSEK
Język ma wpływ na skuteczność rozpoznawania emocji, co jest widoczne w tendencji, że modele trenowane na jednym języku mają ogromne trudności z rozpoznawaniem emocji w innym języku co może być spowodowane tym, że dane były z dwóch zupełnie innych zbiorów. Zbiory trenowane na jednym zbiorze, a testowane na drugim radziły sobie nienajgorzej z emocją "sad" co może dowodzić temu, że emocja smutku wyrażana w obu językach posiada podobne cechy. Modele wykazują wyższą skuteczność, gdy są trenowane i testowane na tym samym zbiorze danych (szczególnie dla zbioru danych w języku angielskim), jest to naturalne zjawisko aczkolwiek zbyt niskie wyniki (praktycznie zerowa precyzja w każdym modelu dla happy i neutral testowanych na języku angielskim i trenowanym na języku polskim) mogą świadczyć również o tym, że cechy emocji wyrażanych w obu językach są inne.

Na podstawie wyników testów (język polski i angielski) modeli trenowanych na języku niemieckim można zauważyć, że w przypadku języka polskiego najlepiej rozpoznawaną emocją jest emocja smutku, potrafiła ona w 5 eksperyemtach osiagnąc precyzję równą 1, emocja złości uzyskiwała niską precyzję w wielu eksperymentach, tylko w jednym (random_forest_emo_db uzyskała precyzję pozwyżej 0.5) Podczas testowania na języku angielskim najlepsze wyniki uzyskano dla emocji złości. Emocja smutku natomiast wynosiła ponizej 0.2 w większości z eksperymentów, z tego wynika, że o ile emocja smutku zawiera podobne cechy w języku polskim i angielskim, cechy te różnią się na tyle, że podczas testowania na modelach, które były trenowane na innym języku emocja ta nie jest rozpoznawana w obu przypadkach.  

Podczas testowania zbiorów nEMO i RAVDESS na modelach trenowanych na zbiorze danych TESS można zauważyć, że zarówno angielski jak i polski zbiór danych najelpiej radzi sobie dla emocji smutku, co może potwierdzać to, że oba języki posiadają najbardziej zbliżone cechy dla tej właśnie emocji. Modele testowane na zbiorze danych RAVDESS osiągały także nienajgorsze wyniki dla emocji "neutral", zgadza się to z wynikami modeli trenowanych i testowanych na zbiorze danych RAVDESS. Wyniki na tym drugim oczywiście są wyższe, co jest naturalnym zjawiskiem dla modeli trenowanych i testowanych na tym samym zbiorze danych. Modele testowane na zbiorze danych nEMO uzyskały lepsze wyniki precyzji (dla emocji smutku) dla modeli trenowanych na zbiorze danych TESS niż na zbiorze danych RAVDESS.
