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
