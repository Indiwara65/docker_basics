import os
from pathlib import Path

list_of_files = [
    "src/__init__.py",
    "src/__main__.py",
    "src/arithmatic.py",
    "src/numpy_arithmatic.py",
    "test/__init__.py",
    "test/integration",
    "test/unit",
    "reqirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    ".gitignore",
    "tox.ini",
    ".github/workflows/ci.yml"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dir, filename = os.path.split(filepath)
    print(f"dir:{dir}\nfilename:{filename}\n")
    if dir != "":
        os.makedirs(dir, exist_ok=True)
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filename, 'w') as f:
            pass