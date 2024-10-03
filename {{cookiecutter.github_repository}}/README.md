# {{ cookiecutter.module_name }}

{{ cookiecutter.module_description }}

Se você vai *desenvolver* deste repositório, vá para o [guia de desenvolvimento](README_DEV.md).

## Instalando {{cookiecutter.module_name}}:

Lembre-se de seguir essas instruções de dentro do seu ambiente virtual preferido:

    conda create -n {{cookiecutter.project_slug}} python={{cookiecutter.python_version}}
    conda activate {{cookiecutter.project_slug}}

A primeira maneira é clonar o repositório e fazer uma instalação local:

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}.git
    cd {{cookiecutter.github_repository}}
    pip install .

A segunda maneira é instalar diretamente

    pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}.git

Para desinstalar, use:

    pip uninstall install {{cookiecutter.project_slug}}

## Uso

Para encontrar todos os comandos implementados, execute:

    {{cookiecutter.project_slug}}-cli --help

