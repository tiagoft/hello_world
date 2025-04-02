# {{ cookiecutter.module_name }}

{{ cookiecutter.module_description }}

If you are going to *develop* from this repository, go to the [development guide](README_DEV.md).

## Installing {{cookiecutter.module_name}}:

Remember to follow these instructions from within your preferred virtual environment:

    conda create -n {{cookiecutter.project_slug}} python={{cookiecutter.python_version}}
    conda activate {{cookiecutter.project_slug}}

The first way  is to clone the repository and do a local installation:

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}.git
    cd {{cookiecutter.github_repository}}
    pip install .

The second way is to install directly:

    pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}.git

To uninstall, use:

    pip uninstall {{cookiecutter.project_slug}}

## Usage

To find all implemented commands, run:

    {{cookiecutter.project_slug}}-cli --help
