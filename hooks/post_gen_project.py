import shutil
import os

language = "{{cookiecutter.language}}"

readme_files = {'pt-br' : 'README_PT.md', 
                'en-us' : 'README_EN.md'}

readme_dev_files = {'pt-br' : 'README_DEV_PT.md', 
                    'en-us' : 'README_DEV_EN.md'}

shutil.copy(readme_files[language], 'README.md')
shutil.copy(readme_dev_files[language], 'README_DEV.md')

for fname in readme_files.items():
    os.unlink(fname[1])

for fname in readme_dev_files.items():
    os.unlink(fname[1])

with open('README_DEV.md', 'r') as file:
    contents = file.read()
    print(contents)