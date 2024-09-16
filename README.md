# hello_world: meu template cookiecutter

## Como usar, bem rapidamente

    pip install cookiecutter
    cookiecutter gh:tiagoft/hello_world

## O que é

**Cookiecutter** é um programa para criar projetos à partir de templates. A vantagem de usar um template é que você pode já deixar toda a estrutura inicial (que geralmente chamamos de boilerplate code) preparada. Isso significa que toda a árevore de diretórios, os arquivos de setup, etc., podem já ficar prontos, o que economiza tempo que você deveria empregar em fazer coisas realmente diferentes.

Este template tem as seguintes *features*:

* Define um aplicativo de linha de comando (CLI) com a biblioteca `typer`;
* O template é inicializado com dois arquivos-fonte Python (e acesso via biblioteca) e acesso a um *asset*, de forma que você pode seguir o exemplo para continuar com um código organizado;
* O template gera um `README.md` com instruções tanto para desenvolvedores quanto para usuários;
* O template traz um arquivo `setup.py` para que seu programa possa ser instalado pelo usuário através de um comando tipo `pip install`.

## Inicializar seu projeto

Dentro do seu venv/conda env:

    pip install cookiecutter
    cookiecutter gh:tiagoft/hello_world

E então insira as instruções pedidas pelo inicializador.

Após a criação, você deverá ver um diretório com o nome do seu projeto. Siga as instruções no README.md que estiver nesse diretório.