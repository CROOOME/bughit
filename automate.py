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

        self.commands = [
            'git add {}'.format('new_file'),    # make_file
            "git commit -m '{}'".format('commit message to be filled here')
        ]

    def root_dir(self):
        if str(os.getcwd()) == str(self.repo_dir):
            print("match:")
            print('cwd:\t{}'.format(str(os.getcwd())))
            print('repo:\t{}'.format(str(self.repo_dir)))
            return
        else:
            print("changing to root dir")
            print("NO match:")
            print('cwd:\t{}'.format(str(os.getcwd())))
            print('repo:\t{}'.format(str(self.repo_dir)))
            os.chdir(str(self.repo_dir))
            self.root_dir()

    def clone_repo(self):
        # clone repo:
        f = os.listdir(str(self.repo_dir.absolute()))
        print(f)
        if self.repo_name not in f:
            # Clone repo
            os.chdir(str(self.repo_dir))
            print("CWD:", os.getcwd())

            clone_repo = "git clone {}".format(self.repo)
            output, error = self.run_command(clone_repo)
            print(output, error)

    def git_add(self, file_name):
        # # Add file to git
        clone_repo = "git add {}".format(file_name)
        output, error = self.run_command(clone_repo)
        print(output, error)

    def make_file(self):
        # make_file

        new_file = 'edits.{}'.format('txt')
        f = open(new_file, "w+")
        f.close()

        print('New file: ', os.path.isfile(new_file))

        #self.git_add(new_file)

    def run_command(self, cmd):
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output, error

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

        if not os.path.exists(str(self.repo_dir)):
            self.clone_repo()

        self.root_dir()
        print(str(self.repo_dir))

        self.make_file()



if __name__ == '__main__':
    bughit = BugHit(DEBUG=False)
    bughit.run()
