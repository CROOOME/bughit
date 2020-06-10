import os
from pathlib2 import Path
import random
import subprocess


# read from file or params
min_commits = 5
max_commits = 20
range_of_commits = random.randrange(min_commits, max_commits)
additions = 10
subtractions = 2
edits = additions + subtractions
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
f = os.listdir(str(repo_dir.absolute()))
print(f)
if repo_name not in f:
    # Clone repo
    os.chdir(str(repo_dir))
    print("CWD:", os.getcwd())

    bashCommand = "git clone {}".format(repo)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output, error)


f = os.listdir(str(repo_dir.absolute()))
print(f)
