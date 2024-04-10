# Cookiecutter template for Data Science projects

This is a straightforward data science template created with Cookiecutter. It streamlines repetitive tasks like folder creation and file organization.

## Getting Started

Before using this template, ensure that you have Python installed on your computer, WSL, or a virtual environment.

### Installing cookicutter

Visit the official [website](https://cookiecutter.readthedocs.io/en/latest/installation.html) to learn how to install and configure Cookiecutter. 
If you’re using pip, run the following command in your console:

    pip install cookiecutter

## Creating your project 

1. Open a command terminal.
2. Navigate to your project folder.
3. Execute the following command:

        cookiecutter https://github.com/yeimmygit11/cookiecutter_personal.git

If Cookiecutter was installed correctly, the command line will prompt you for some data to generate your project. These include:

  - **project_name** : he desired name for your project.
  - **project_slug** : A nickname for your project (usually the project name in lowercase with underscores).
  - **project_description** : A brief description of your project.
  - **project_author_name** : Your name or the organization’s name associated with the project.
  - **python_version**: By default, Python 3.10.
  - **project_packages** : Choose between “All” or “Minimal.”

  As a result, you will have a project template with the following folders:

  - Data
  - Notebooks
  - Reports
  - figures
  - Src

Additionally, the template will automatically generate the following files:

  - README.md: This file will contain the information you provided during setup.
  - requirements.txt : This file is a simple text file that lists all the dependencies (libraries or packages) your project requires.
  
    For installing the packages automatically you can run the next command :

        pip install -r requirements.txt
   


## Authors
  - **Yeimmy Morales** 





