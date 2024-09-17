import sys
import subprocess

def is_git_installed() -> bool:
    print("Checking if Git is installed...")
    try:
        subprocess.run(["git",  "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if not is_git_installed():
        print("ERROR: Git is not installed. Use `apt install git` before proceeding!")
        sys.exit(1)
    else:
        print("Git is installed.")
    exit(1)
    print("All requirements are met. You can proceed.")

