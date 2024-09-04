from setuptools import setup, find_packages

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hello_world",  # Substitua pelo nome do seu pacote
    version="0.1.0",
    author="Tiago Tavares",
    author_email="tiagoft@gmail.com",
    description="Um pacote minimalista em python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joao-Gabriel05/hello_world",  # URL do repositório do seu projeto (se houver)
    packages=find_packages(),  # Encontra automaticamente todos os pacotes no diretório
    package_data={
    '': [
        'assets/*.txt',
    ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.6',
    entry_points={
        'console_scripts': [
            'enigma=enigma.main:main',
        ],
    },
    install_requires=[  # Instala as dependências especificadas no requirements.txt
        line.strip() for line in open("requirements.txt").readlines()
    ],
)
