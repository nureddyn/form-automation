import os
from .path_handling import *
from typing import List, Any, Dict
from .classes.File import File
from modules.file_formats import data_formats
from .buffer import *
from .reader import *
from .writer import *

"""
Validate file according to process of transport data from a spreadsheet to word/pdf
"""

# TODO: Validate files using a valid_extension (done), a valid_data_file (to check if the content format is correct) and a valid_template_file()

def get_input_file_list() -> List[File]:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_directory = os.path.join(current_directory, '..', 'input')
    file_list = os.listdir(input_directory)

    files = []

    for file in file_list:
        full_path = os.path.join(input_directory, file)
        file = File(full_path)
        print(is_valid_format(file))
        if valid_extension(file) and is_valid_format(file):
            files.append(file)
    return files


def valid_extension(file: File) -> bool:
    if file.extension in [".csv", ".xlsx", ".gsheet", ".pdf"]:
        return True
    # raise ValueError("File extension not allowed")


# TODO: This function must make a distinction between input and template files
def is_valid_format(file: File) -> bool:
    # Read the file and check if the format comply with predefined conventions
    file_buffer = file_reader(file)
    file_buffer_keys = file_buffer.keys()

    for format in data_formats:
        if format.keys() == file_buffer_keys and file_buffer.get('TYPE') == format.get('TYPE'):
            return True
    return False

# TODO: Create a function that determines which template will be used.
def data_file_format(file: File) -> str:
    return

def get_file_type(file: File) -> str:
    if file.extension in [".csv", ".xlsx", ".gsheet"]:
        return 'Data file'
    elif file.extension in [".docx", ".pdf"]:
        return 'Template file'
    raise ValueError("File type not allowed")


# TODO: Pull the most recent forms from source to 'templates' folder
def update_templates():
    return


def generate_forms(input_files: List[File]):

    # update_templates()

    # TODO: Ensure the template file can be scanned to get the form type
    templates_folder = get_absolute_path('templates')
    templates_list = os.listdir(templates_folder)
    template_files = [File(os.path.join(templates_folder, template)) for template in templates_list]
    print(input_files)
    for file in input_files:
        input_buffer = file_reader(file)
        required_form_type = input_buffer.get('TYPE')

        required_template = next(
            (template for template in template_files
             if file_reader(template) and 
             file_reader(template).get('TYPE').strip() == required_form_type.strip()),
              None
              )
        file_writer(input_buffer, required_template)


# TODO: Implement writer functionality for docx
def file_writer(buffer, template: File):
    try:
        if template.extension == ".pdf":
            write_to_pdf(buffer, template)
        else:
            raise NotImplementedError("writing to docx is not implemented yet.")
    except Exception as e:
        raise Exception(f"{e}")


