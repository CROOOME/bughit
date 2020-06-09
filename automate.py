
import os
from pathlib2 import Path
import random


# read from file or params
repo = 'https://github.com/CROOOME/automated_bughit.git'
repo_dir = None

# Checks
if repo_dir is None:
    print("Moving one level up..")
    print("{} -> {}".format(current_path, parent_path))
    repo_dir = parent_path
    print("repo_dir:", repo_dir)


# clone repo:
print(os.getcwd())
