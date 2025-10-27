"""
Smoke-test script: attempts to import key libraries and run a minimal operation for each.
This script intentionally catches ImportError and other exceptions and prints a clear pass/fail report.
Run with: python smoke_test.py
"""

import sys
import importlib

packages = [
    ("numpy", "import numpy as np; np.array([1,2,3])"),
    ("pandas", "import pandas as pd; pd.DataFrame({'a':[1]})"),
    ("matplotlib", "import matplotlib; matplotlib.__version__"),
    ("sklearn", "import sklearn; sklearn.__version__"),
    ("scipy", "import scipy; scipy.__version__"),
    ("cv2", "import cv2; cv2.__version__"),
    ("PIL", "from PIL import Image; Image.new('RGB', (2,2))"),
    ("scikit_image", "import skimage; skimage.__version__"),
    ("tensorflow", "import tensorflow as tf; tf.constant([1.0])"),
    ("torch", "import torch; torch.tensor([1.0]).sum()"),
    ("torchvision", "import torchvision; torchvision.__version__"),
    ("jupyter", "import jupyter; getattr(jupyter, '__version__', 'n/a')"),
]

results = []

print('Running smoke-test imports...')
for name, code in packages:
    try:
        # Execute code string in an isolated namespace
        ns = {}
        exec(code, ns, ns)
        results.append((name, True, None))
        print(f'  OK: {name}')
    except Exception as e:
        results.append((name, False, str(e)))
        print(f'  FAIL: {name} -> {e.__class__.__name__}: {e}')

print('\nSummary:')
ok = [r for r in results if r[1]]
fail = [r for r in results if not r[1]]
print(f'  Passed: {len(ok)}')
for r in ok:
    print(f'    - {r[0]}')
print(f'  Failed: {len(fail)}')
for r in fail:
    print(f'    - {r[0]}: {r[2]}')

# Exit code: 0 if all passed, otherwise 2
sys.exit(0 if len(fail) == 0 else 2)
