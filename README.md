# Lung Cancer Detection

This repository contains Jupyter notebooks, pre-trained model artifacts, and scripts used to train and evaluate models for lung/colon histology and CT-scan image classification.

## Repository status

- Most analysis and training code lives in notebooks in the repo root (e.g. `CancerDetect.ipynb`, `CancerDetectTorch.ipynb`, `CancerDetectEffiNet.ipynb`, ...).
- Large model files (`*.pth`, `*.h5`) are tracked in the repository root. Consider using Git LFS or removing them from the repository if you intend to publish the code.

## Expected dataset layout (relative to repository root)

The notebooks expect the dataset to be available under `lung_colon_image_set/lung_image_sets` and `lung_colon_image_set/colon_image_sets`.

This repository now includes placeholder folders to mirror the backup dataset structure. Populate them by copying the dataset into the following paths:

- `lung_colon_image_set/`

  - `lung_image_sets/`
    - `lung_aca/` (adenocarcinoma)
    - `lung_n/` (normal)
    - `lung_scc/` (squamous cell carcinoma)
  - `colon_image_sets/`
    - `colon_aca/`
    - `colon_n/`

- `LungHistology/images/`

  - `aca_bd/`, `aca_md/`, `aca_pd/`, `nor/`, `scc_bd/`, `scc_md/`, `scc_pd/`

- `data/` (general-purpose data and CSVs such as `data.csv`)

If you keep the original dataset elsewhere (e.g., a backup drive), you can either copy the folders into the repo, or create a symlink from the expected path to the backup location. Example (Windows PowerShell):

```powershell
New-Item -ItemType SymbolicLink -Path .\lung_colon_image_set -Target "F:\Puneet Verma\System BackUp\Lung Cancer Detection\lung_colon_image_set"
```

(Requires Developer mode or Administrator privileges.)

## Backup dataset location

The following backup location and structure were provided and match the placeholders above:

F:\Puneet Verma\System BackUp\Lung Cancer Detection

- .venv/
- data/
- LungHistology/
  - images/
    - aca_bd/
    - aca_md/
    - aca_pd/
    - nor/
    - scc_bd/
    - scc_md/
    - scc_pd/
  - data.csv
- lung_colon_image_set/
  - colon_image_sets/
    - colon_aca/
    - colon_n/
  - lung_image_sets/
    - lung_aca/
    - lung_n/
    - lung_scc/

If you'd like, I can add a small script to copy or validate dataset files from that backup location into the repository structure.

## Kaggle dataset links

Please paste the dataset download links here so others can reproduce the setup. Example entries:

- Lung/Colon image set (Kaggle):

  - [Kaggle dataset name or URL goes here]

- Additional dataset (e.g., Lung Histology):
  - [Kaggle dataset name or URL goes here]

## How to run (quick)

1. Create a Python environment and install dependencies (see `requirements.txt` if present).
2. Place dataset under `lung_colon_image_set/` as described above.
3. Open the chosen notebook in Jupyter and run the cells, or use converted scripts (notebooks currently contain the runnable code).

## Notes & recommendations

- Add a `requirements.txt` or environment file. I can generate a proposed `requirements.txt` from the notebooks' imports.
- Consider moving large model files out of the repository and into cloud storage or use Git LFS.
- Convert the main notebooks into standalone `train_*.py` scripts for reproducibility.

---

If you want, I can now extract imports from all notebooks and create a `requirements.txt`, plus add a small `train_torch.py` runner that uses dummy data to smoke-test imports.
