import os
from pathlib import Path
from rich.console import Console
import typer
import {{cookiecutter.project_slug}} as {{cookiecutter.module_abbreviation}}

app = typer.Typer(no_args_is_help=True)
console = Console()

@app.command('info')
def print_info(custom_message : str = ""):
    """
    Print information about the module
    """
    console.print("Hello! I am {{cookiecutter.module_name}}")
    console.print(f"Author: { {{cookiecutter.module_abbreviation}}.__author__}")
    console.print(f"Version: { {{cookiecutter.module_abbreviation}}.__version__}")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")

@app.command('demo') # Defines a default action
def run():
    """
    This is a demonstration function that shows how to use the module
    """
    print("Hello world!")
    {{cookiecutter.module_abbreviation}}.my_function()
    script_path = Path(os.path.abspath(__file__))
    parent_path = script_path.parent
    print("Script path:", script_path)
    with open(parent_path / "assets/poetry.txt") as f:
        print(f.read())
    with open(parent_path / "assets/test_folder/test_something.txt") as f:
        print(f.read())

if __name__ == "__main__":
    app()