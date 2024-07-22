**nEMO** - język polski
**RAVDESS** - język angielski

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
Emocja "happy" osiągnęła precyzję 0.0 w wielu eksperymentach: MLP_from_git_updated_nEMO, SVC_linear_nEMO, SVC_nEMO, SVC_with_LDA_nEMO, SVC_with_PCA_nEMO, knn_lda_nEMO.

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

# WNIOSEK
Język ma wpływ na skuteczność rozpoznawania emocji, co jest widoczne w tendencji, że modele trenowane na jednym języku mają ogromne trudności z rozpoznawaniem emocji w innym języku co może być spowodowane tym, że dane były z dwóch zupełnie innych zbiorów. Zbiory trenowane na jednym zbiorze, a testowane na drugim radziły sobie nienajgorzej z emocją "sad" co może dowodzić temu, że emocja smutku wyrażana w obu językach posiada podobne cechy. Modele wykazują wyższą skuteczność, gdy są trenowane i testowane na tym samym zbiorze danych (szczególnie dla zbioru danych w języku angielskim), jest to naturalne zjawisko aczkolwiek zbyt niskie wyniki (praktycznie zerowa precyzja w każdym modelu dla happy i neutral testowanych na języku angielskim i trenowanym na języku polskim) mogą świadczyć również o tym, że cechy emocji wyrażanych w obu językach są inne.
