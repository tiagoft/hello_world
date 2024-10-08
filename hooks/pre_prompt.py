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

def get_python_version() -> str:
    print("Checking Python version...")
    try:
        result = subprocess.run(["python", "--version"], capture_output=True, check=True, text=True)
        version = result.stdout.strip()
        version = '.'.join(version.split(' ')[1].split('.')[0:2])
        return version
    except:
        print("ERROR: Unable to get Python version.")
        return False

if __name__ == "__main__":
    if not is_git_installed():
        print("ERROR: Git is not installed. Use `apt install git` before proceeding!")
        sys.exit(1)
    else:
        print("Git is installed.")


    new_context = {}
    git_user_name = get_git_user_name()
    if git_user_name is not False:
        new_context['author_name'] = git_user_name
    
    git_user_email = get_git_user_email()
    if git_user_email is not False:
        new_context['author_email'] = git_user_email

        git_username = git_user_email.split('@')[0]
        new_context['github_username'] = git_username

    python_version = get_python_version()
    new_context['python_version'] = python_version

    # Load cookiecutter.json
    with open('cookiecutter.json', 'r') as file:
        context = json.load(file)

    context.update(new_context)

    with open('cookiecutter.json', 'w') as file:
        json.dump(context, file, indent=4)

    print("All requirements are met. You can proceed.")

