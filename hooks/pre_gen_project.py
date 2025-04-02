import sys
import subprocess

STATUS_OK = 0
ERROR_REPO_NOT_EMPTY = 1
ERROR_REPO_DOES_NOT_EXIST = 2

repo = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository }}"

def check_if_repository_exists_and_is_empty() -> int:
    print(f"Checking if repository: {repo} exists and is empty...")
    try:
        ret = subprocess.run(["git", "ls-remote", f"{repo}"],
                             capture_output=True,
                             check=True)
        nchars = len(ret.stdout)
        if nchars == 0:
            return STATUS_OK
        else:
            return ERROR_REPO_NOT_EMPTY

    except Exception:
        return ERROR_REPO_DOES_NOT_EXIST

if __name__ == "__main__":
    status = check_if_repository_exists_and_is_empty()
    if status == ERROR_REPO_DOES_NOT_EXIST:
        print(f"WARNING: Repository does not exist.\nPlease create repository {repo} on GitHub before proceeding!")
        print(f"Visit https://github.com/{{ cookiecutter.github_username }}")
        print(f"or use the GitHub CLI: gh repo create {{ cookiecutter.github_repository }}")
    elif status == ERROR_REPO_NOT_EMPTY:
        print(f"WARNING: Repository is not empty. Please delete and restart repository {repo} on GitHub before proceeding!")
        
    print("Proceeding with creating the directory.")
