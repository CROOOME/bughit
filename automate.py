import os
from pathlib2 import Path
import random
import subprocess


# read from file or params
per_push_min_commits = 5
per_push_max_commits = 20
per_push_range_of_commits = random.randrange(per_push_min_commits, per_push_max_commits)
per_commit_additions = 10
per_commit_subtractions = 2
per_commit_edits = per_commit_additions + per_commit_subtractions

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
