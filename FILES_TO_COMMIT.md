# Files to commit to this GitHub repository

This file lists the recommended files and folders to keep under version control in this repository.
Large model binaries and datasets should be kept outside of the repository (use Git LFS or cloud storage) — see notes below.

Core files to include in GitHub

- `README.md` (project description, dataset links, how to run)
- `requirements.txt` (minimal, flexible deps) and/or `requirements-pinned.txt` (exact pins)
- `smoke_test.py` (environment validation script)
- `*.ipynb` notebooks containing analysis and experiments (e.g., `CancerDetect.ipynb`, `CancerDetectTorch.ipynb`)
- Any `*.py` scripts for training/inference that you add (e.g., `train_torch.py`, `predict.py`)
- `FILES_TO_COMMIT.md` (this manifest)
- `.gitignore` and other repo helper files (`.gitattributes`, `LICENSE`)

Files to keep out of Git and store elsewhere

- Dataset directories and image files:
  - `lung_colon_image_set/` (use a dataset download or backup location)
  - `LungHistology/` and `data/`
- Large model artifacts and checkpoints:
  - `*.pth`, `*.pt`, `*.h5` — move to `models/` and track with Git LFS or upload to cloud storage (AWS S3, Google Drive, etc.)

Suggested layout for storing large artifacts (not recommended in main repo):

- `models/` (store only small checkpoints or metadata; add to LFS if necessary)
- `data/` (not tracked; instruct users how to download externally or symlink to backup)

If you want some smaller, exportable model artifacts in the repository (e.g., a converted `model.onnx` under 50MB for demo), add them under `models/` and record them here with size and purpose.

How to add large files safely

- Use Git LFS. Example (install and track `*.pth`):

  - `git lfs install`
  - `git lfs track "*.pth"`
  - Commit the `.gitattributes` file

- Or store model files in cloud storage and add a small `models/README.md` listing download URLs and expected filenames.

If you'd like, I can:

- Create a `models/README.md` with download links and small metadata for each model file currently in the repo.
- Initialize a `.gitattributes` file that tracks `*.pth` with Git LFS (note: LFS must be enabled on the remote repository).
