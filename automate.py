import os
from pathlib2 import Path
import random


# read from file or params
repo = 'https://github.com/CROOOME/automated_bughit.git'
repo_name = repo.split("/")[-1].split(".")[0]
repo_dir = None

current_path = Path.cwd()
parent_path = current_path.parent

# Checks
if repo_dir is None:
    print("Moving one level up..")
    print("{} -> {}".format(current_path, parent_path))
    repo_dir = parent_path
    print("repo_dir:", repo_dir)


# clone repo:
print(os.getcwd())
