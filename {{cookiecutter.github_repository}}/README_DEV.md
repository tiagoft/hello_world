
# Guia para desenvolvedores

## Configurando seu ambiente de trabalho

Execute estas instruçõess imediatamente após criar seu projeto com o cookiecutter.

1. Navegue para o diretório que você criou

        cd {{cookiecutter.module_slug}}

2. Crie um ambiente virtual para seu desenvolvimento:

        conda create -n {{cookiecutter.module_slug}} python={{cookiecutter.python_version}}
        conda activate {{cookiecutter.module_slug}}

3. (opcional) Instale o aplicativo `gh` para criar automaticamente seu repositório no GitHub:

        conda install gh --channel conda-forge
        gh auth login

4. Instale seu módulo em modo editável:

        pip install -e .

5. Verifique que a ferramenta de linha de comando está funcionando:

        {{cookiecutter.module_slug}}-cli --help

## Sincronizando com Github

### Com o aplicativo `gh`

Na pasta-raiz de seu projeto recém-criado:

    git init
    git add *
    git commit -m "Commit inicial"
    gh repo create {{ cookiecutter.github_repository}} --public --push --source .

### Sem o aplicativo `gh`

1. Em seu navegador, vá para o [GitHub](https://www.github.com) e faça login como {{ cookiecutter.github_username}}
1. Crie um novo repositório (vazio, sem README inicial, sem gitignore, etc) chamado {{ cookiecutter.github_repository}} (lembre-se de respeitar maiúsculas, minúsculas, etc).
1. Execute os comandos abaixo na pasta-raiz de seu projeto recém-criado:


        git init
        git add *
        git commit -m "Commit inicial"
        git remote add origin https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.github_repository}}.git
        git push --set-upstream origin main


