**nEMO** - język polski
**RAVDESS** - język angielski

## Testowanie na nEMO modeli trenowanych na RAVDESS
- większość modeli ma trudności z rozpoznawaniem emocji z precyzją powyżej 0.5. Żadna emocja nie osiągnęła precyzji powyżej 0.5 w żadnym z eksperymentów
-  najlepiej rozpoznawaną emocją jest zazwyczaj "happy" (szczęśliwy) lub "sad" (smutny)
-  "Happy" uzyskało najwyższą precyzję w kilku eksperymentach (0.24, 0.25), ale nigdy nie przekroczyło 0.5
-  "Sad" uzyskało nieco wyższą precyzję w niektórych eksperymentach, osiągając najwyższą wartość 0.41
- "Angry" (zły), "neutral" (neutralny) i "sad" często miały precyzję poniżej 0.2 w wielu eksperymentach
- "Angry" i "neutral" były często rozpoznawane z precyzją równą 0.0, co oznacza całkowite niepowodzenie w ich identyfikacji
## Testowanie na nEMO modeli trenowanych na nEMO
- emocją, która jest najlepiej rozpoznawana w prawie wszystkich eksperymentach, jest "sad" (smutny). Precyzja w rozpoznawaniu tej emocji jest bardzo wysoka, często osiągając wartości bliskie 1.0 (100%)
- w zdecydowanej większości eksperymentów jedyną emocją, która osiągnęła precyzję powyżej 0.5, jest "sad"
- większość emocji rozpoznawana jest na poziomie powyżej 0.2 ale poniżej 0.5 (z dwoma wyjątkami „happy”)
##Testowanie na nEMO modeli trenowanych na RAVDESS i nEMO
- emocja "sad" (smutny) jest najlepiej rozpoznawana w większości eksperymentów. Precyzja rozpoznawania tej emocji jest bardzo wysoka, często osiągając wartości bliskie 1.0 (100%)
- modele radzą sobie również dobrze z rozpoznawaniem emocji "neutral"

## Testowanie na RAVDESS modeli trenowanych na nEMO
- emocja "sad" (smutny) jest najlepiej rozpoznawana w wielu eksperymentach (precyzja zazwyczaj powyżej lub równa 0.5)
- emocje "happy" (szczęśliwy) i "neutral" (neutralny) mają precyzję poniżej 0.2 w wielu eksperymentach
- precyzja rozpoznawania emocji "neutral" wynosi 0.0 w większości eksperymentów
- emocja "happy" osiągnęła precyzję 0.0 w wielu eksperymentach
## Testowanie na RAVDESS modeli trenowanych na RAVDESS
- zbiór danych RAVDESS oraz zastosowane modele są skuteczne w rozpoznawaniu różnych emocji, osiągając precyzję powyżej 0.5 dla wszystkich emocji w większości eksperymentów
- najwyższą precyzje zazwyczaj mają emocje angry i neutral
- żaden z modeli nie ma trudności z rozpoznawaniem emocji poniżej precyzji 0.2
## Testowanie na RAVDESS modeli trenowanych na nEMO i RAVDESS
- wszystkie emocje ("angry", "happy", "neutral", "sad") osiągnęły precyzję powyżej 0.5 w większości eksperymentów
- w żadnym z eksperymentów nie ma emocji z precyzją poniżej 0.2

# WNIOSEK
Język ma wpływ na skuteczność rozpoznawania emocji, co jest widoczne w tendencji, że modele trenowane na jednym języku mają trudności z rozpoznawaniem emocji w innym języku. Najlepiej rozpoznawaną emocją w obu językach jest "sad", natomiast emocje "angry" i "neutral" są najtrudniejsze do rozpoznania, szczególnie przy zmianie języka. Modele wykazują wyższą skuteczność, gdy są trenowane i testowane na tym samym zbiorze danych, co sugeruje, że zawierają one specyficzne cechy zależne od języka.

