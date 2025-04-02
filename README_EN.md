# hello_world: my cookiecutter template

## How to use it, very quickly

    pip install cookiecutter
    cookiecutter gh:tiagoft/hello_world

## What it is

**Cookiecutter** is a program to create projects from templates. The advantage of using a template is that you can have the entire initial structure (which we usually call boilerplate code) ready. This means that the directory tree, setup files, etc., can already be prepared, saving you time that you can use to work on truly unique things.

This template has the following *features*:

* Defines a command-line interface (CLI) application using the `typer` library;
* The template is initialized with two Python source files (with access via library) and access to an *asset*, allowing you to follow the example to keep your code organized;
* The template generates a `README.md` with instructions for both developers and users;
* The template includes a `setup.py` file so that your program can be installed by users with a `pip install` command.

## Initialize your project

Within your venv/conda env:

    pip install cookiecutter
    cookiecutter gh:tiagoft/hello_world

Then enter the requested information during initialization.

After creation, you should see a directory with your project's name. Follow the instructions in the README.md located in that directory.