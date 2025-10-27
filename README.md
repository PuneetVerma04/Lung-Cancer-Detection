# Lung Cancer Detection

This repository contains Jupyter notebooks, pre-trained model artifacts, and scripts used to train and evaluate models for lung/colon histology and CT-scan image classification.

## Repository status

- Most analysis and training code lives in notebooks in the repo root (e.g. `CancerDetect.ipynb`, `CancerDetectTorch.ipynb`, `CancerDetectEffiNet.ipynb`, ...).

## Expected dataset layout (relative to repository root)

The notebooks expect the dataset to be available under `lung_image_dataset/lung_image_sets`

This repository now includes placeholder folders to mirror the backup dataset structure. Populate them by copying the dataset into the following paths:

- `lung_image_dataset/`

  - `lung_image_sets/`
    - `lung_aca/` (adenocarcinoma)
    - `lung_n/` (normal)
    - `lung_scc/` (squamous cell carcinoma)

## Kaggle dataset links

- Lung/Colon image set (Kaggle):

  - https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images

## How to run (quick)

1. Create a Python environment and install dependencies (see `requirements.txt` if present).
2. Place dataset under `lung_colon_image_set/` as described above.
3. Open the chosen notebook in Jupyter and run the cells, or use converted scripts (notebooks currently contain the runnable code).
