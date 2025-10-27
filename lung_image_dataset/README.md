Dataset: Lung and Colon Cancer Histopathological Images

This folder is intended to contain the Lung/Colon histopathology image dataset used by the notebooks in this repository.

Source (Kaggle): https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images

Do not commit the image files into this repository. Instead:

- Download the dataset from the Kaggle link above and extract into this folder so the expected structure matches the notebooks (e.g., `lung_image_sets/`, `colon_image_sets/`).
- Or create a symlink from this path to a backup location.

Example (PowerShell) to create a symlink to your backup dataset:

New-Item -ItemType SymbolicLink -Path .\lung_colon_image_set -Target "F:\Puneet Verma\System BackUp\Lung Cancer Detection\lung_colon_image_set"

(Requires Developer mode or Administrator privileges.)
