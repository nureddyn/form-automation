# modules/private_formats.py
import os
from modules.classes.File import File
from modules.reader import file_reader
from modules.path_handling import get_absolute_path

templates_folder = get_absolute_path('templates')
templates_path_list = os.listdir(templates_folder)

# Get the templates format from template file
data_formats = []

for template_path in templates_path_list:
    path = os.path.join(templates_folder, template_path)
    file_buffer = file_reader(File(path))
    format = {}
    format['TYPE'] = file_buffer['TYPE']
    format = {**format, **file_buffer['fields']}

    data_formats.append(format)


"""
example:
data_formats = [
    {
        'TYPE': TYPE,
        'Name': '',
        'Phone': '',
        'Email': '',
        'Country': '',
    },
    {'form-type': 'f2', 'd': ''}
]
"""