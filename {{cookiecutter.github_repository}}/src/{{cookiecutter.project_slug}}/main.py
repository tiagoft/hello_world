"""
{{cookiecutter.module_name}} - {{cookiecutter.module_description}}
Made from cookiecutter template:
cookiecutter gh:tiagoft/hello_world
"""

import importlib.resources
from rich.console import Console
import typer
{% if cookiecutter.project_slug == cookiecutter.module_abbreviation %}
import {{cookiecutter.project_slug}}
{% else %}
import {{cookiecutter.project_slug}} as {{cookiecutter.module_abbreviation}}
{% endif %}

import {{cookiecutter.project_slug}}.my_lib

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
    {{cookiecutter.module_abbreviation}}.my_lib.my_function()
    asset_file = importlib.resources.open_text('{{cookiecutter.module_abbreviation}}.assets', 'poetry.txt')
    print(asset_file.read())
    asset_file = importlib.resources.open_text('{{cookiecutter.module_abbreviation}}.assets.test_folder', 'test_something.txt')
    print(asset_file.read())

if __name__ == "__main__":
    app()
