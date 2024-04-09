import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
ERROR_COLOR = "\x1b[31m"

module_name = '{{ cookiecutter.project_title }}'

if not re.match(MODULE_REGEX, module_name):
    print(f'{ERROR_COLOR}ERROR: {module_name} is not a valid Python module name!')
    raise ValueError(f'{module_name} is not a valid Python module name!')


else:
    print("Starting the template generation using Cookiecutter!.")