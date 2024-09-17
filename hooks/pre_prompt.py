import sys
import subprocess
import json

def is_git_installed() -> bool:
    print("Checking if Git is installed...")
    try:
        subprocess.run(["git",  "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False
    
def get_git_user_name() -> str:
    print("Getting Git user name...")
    try:
        result = subprocess.run(["git", "config", "--get", "user.name"], capture_output=True, check=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"ERROR: Unable to get Git user name. {e}")
        return False

def get_git_user_email() -> str:
    print("Getting Git user email...")
    try:
        result = subprocess.run(["git", "config", "--get", "user.email"], capture_output=True, check=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"ERROR: Unable to get Git user email. {e}")
        return False

if __name__ == "__main__":
    if not is_git_installed():
        print("ERROR: Git is not installed. Use `apt install git` before proceeding!")
        sys.exit(1)
    else:
        print("Git is installed.")

    # Load cookiecutter.json
    with open('cookiecutter.json', 'r') as file:
        context = json.load(file)

    git_user_name = get_git_user_name()
    git_user_email = get_git_user_email()

    new_context = {}

    new_context['author_name'] = git_user_name
    new_context['author_email'] = git_user_email

    context.update(new_context)

    with open('cookiecutter.json', 'w') as file:
        json.dump(context, file, indent=4)

    print("All requirements are met. You can proceed.")

