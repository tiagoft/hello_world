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
        print(f"ERROR: Repository does not exist.\nPlease create repository {repo} on GitHub before proceeding!")
        sys.exit(1)
    elif status == ERROR_REPO_NOT_EMPTY:
        print(f"ERROR: Repository is not empty. Please delete and restart repository {repo} on GitHub before proceeding!")
        sys.exit(1)

    print("All requirements are met. You can proceed.")
