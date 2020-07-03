import os
from pathlib2 import Path
import random
import subprocess


class BugHit:
    def __init__(self, DEBUG=False):
        # import settings or use these as defaults
        self.DEBUG = DEBUG
        self.per_push_min_commits = 5
        self.per_push_max_commits = 20
        self.per_push_range_of_commits = random.randrange(self.per_push_min_commits, self.per_push_max_commits)

        self.per_commit_additions = 10
        self.per_commit_subtractions = 2
        self.per_commit_edits = self.per_commit_additions + self.per_commit_subtractions

        self.current_path = Path.cwd()
        self.parent_path = self.current_path.parent

        # dummy repo we will use to make commits
        self.repo = 'https://github.com/CROOOME/automated_bughit.git'
        self.repo_name = self.repo.split("/")[-1].split(".")[0]             # default: repo_name [excluding extension]
        self.repo_dir = Path.joinpath(self.parent_path, self.repo_name)

    def clone_repo(self):
        # clone repo:
        f = os.listdir(str(self.repo_dir.absolute()))
        print(f)
        if self.repo_name not in f:
            # Clone repo
            os.chdir(str(self.repo_dir))
            print("CWD:", os.getcwd())

            bashCommand = "git clone {}".format(self.repo)
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

            print(output, error)

    def sample(self):
        try:
            os.chdir(str(self.repo_path))
            print(os.getcwd())
        except:
            raise NameError('Cannot move to path: ', str(self.repo_path))

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
