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


repo_path = Path.joinpath(repo_dir, repo_name)
print(repo_path)

try:
    os.chdir(str(repo_path))
    print(os.getcwd())
except:
    raise NameError('Cannot move to path: ', str(repo_path))


# make a new file

class BugHit:
    def __init__(self, DEBUG=False):
        # import settings or use these as defaults
        self.DEBUG = DEBUG
        self.per_push_min_commits = 5
        self.per_push_max_commits = 20
        self.per_push_range_of_commits = random.randrange(per_push_min_commits, per_push_max_commits)

        self.per_commit_additions = 10
        self.per_commit_subtractions = 2
        self.per_commit_edits = per_commit_additions + per_commit_subtractions

        self.current_path = Path.cwd()
        self.parent_path = current_path.parent

        # dummy repo we will use to make commits
        self.repo = 'https://github.com/CROOOME/automated_bughit.git'
        self.repo_name = repo.split("/")[-1].split(".")[0]
        self.repo_dir = Path.joinpath(self.parent_path, self.repo_name)

    def clone_repo(self):
        # clone repo:
        f = os.listdir(str(self.repo_dir.absolute()))
        print(f)
        if repo_name not in f:
            # Clone repo
            os.chdir(str(repo_dir))
            print("CWD:", os.getcwd())

            bashCommand = "git clone {}".format(repo)
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

            print(output, error)

    def run(self):
        print('Luckycharms starting...')

        if self.DEBUG:
            print('DEBUG....')
            exit(1)
        if not os.path.exists(self.repo_dir):
            self.clone_repo()



if __name__ == '__main__':
    bughit = BugHit(DEBUG=True)
    bughit.run()
