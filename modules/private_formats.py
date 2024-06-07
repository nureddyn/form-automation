# modules/private_formats.py
import os
from modules.classes.File import File
from modules.reader import file_reader
from modules.path_handling import get_absolute_path

templates_folder = get_absolute_path('templates')
templates_list = os.listdir(templates_folder)

template_files = []
for template in templates_list:
    new_template = os.path.join(templates_folder, template)
    template_files.append(File(new_template))

# TODO: create functionality to get every field from each template in templates folder
TYPE = ''
if len(template_files) > 0:
    TYPE = file_reader(template_files[0])['TYPE']

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
