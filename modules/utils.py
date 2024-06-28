import os
import subprocess
import platform
import random
import re
from .path_handling import *
from typing import List, Any, Dict
from .classes.File import File
from modules.file_formats import data_formats
from .buffer import *
from .reader import *
from .writer import *
from .models.forms import FORMS


def get_spreadsheet_file(department, form_name: str) -> File:
    spreadsheet_path = get_absolute_path("output")
    spreadsheet_file_list = os.listdir(spreadsheet_path)
    spreadsheet_file = None

    template_path = get_absolute_path("templates")
    templates_path_list = os.listdir(template_path)
    template_files = [os.path.splitext(template)[0] for template in templates_path_list]

    for base_name in spreadsheet_file_list:
        name, _ = os.path.splitext(base_name)
        if name in template_files:
            spreadsheet_file = File(os.path.join(spreadsheet_path, base_name))
    return spreadsheet_file


def get_form_file(department, form_name: str) -> File:
    folder_path = get_absolute_path("templates")
    file_list = os.listdir(folder_path)
    form_file = None
    for name in file_list:
        if name == FORMS[department]["forms"][form_name]:
            form_file = File(os.path.join(folder_path, name))
    return form_file


"""
    This function may execute a script that uses 'wget' or 'curl' command
"""
def fetch_form(department:str, form_name: str):
    templates_path = get_absolute_path("templates")

    if FORMS[department] and form_name in FORMS[department]["forms"].keys():
        form_url = f"{FORMS[department]["url"]}{FORMS[department]["forms"][form_name]}"

        try:
            # Ensure the destination folder exists
            os.makedirs(templates_path, exist_ok=True)

            # Get the filename from the URL
            filename = os.path.basename(form_url)
            file_path = os.path.join(templates_path, filename)

            # Determine fetch command based on operating system
            system = platform.system()
            if system == "Windows":
                # Construct the url command
                command = ["curl", "-o", file_path, form_url]
            elif system == "Linux":
                command = ["wget", form_url, "-P", templates_path]
            else:
                raise Exception(f"Unsupported operating system: {system}")

            # Execute wget or curl command
            result = subprocess.run(command, capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                print(f"File downloaded successfully to {file_path}")
            else:
                print(f"Failed to download file. Error: {result.stderr}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("form not found")


# Function that scans a folder and returns a list of files
def get_file_list(folder_name: str) -> List[File]:
    folder_path = get_absolute_path(folder_name)
    file_list = os.listdir(folder_path)

    folder_file_list = [File(os.path.join(folder_path, template)) for template in file_list]
    
    return folder_file_list


def generate_forms(input_files: List[File]):

    # update_templates()

    # TODO: Ensure the template file can be scanned to get the form type
    templates_path = get_absolute_path('templates')
    templates_list = os.listdir(templates_path)
    template_files = [File(os.path.join(templates_path, template)) for template in templates_list]
    # print(input_files)
    for file in input_files:
        input_buffer = file_reader(file)
        required_form_type = input_buffer.get('TYPE')

        required_template = next(
            (template for template in template_files
             if file_reader(template) and 
             file_reader(template).get('TYPE').strip() == required_form_type.strip()),
              None
              )
        # print(get_template_fields(required_template))
        # TODO: Fix this function:
        # file_writer(input_buffer, required_template)




def get_template_fields(file: File) -> Dict:
    reader = file_reader(file)['fields']
    return reader


def get_input_file_list() -> List[File]:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_directory = os.path.join(current_directory, '..', 'input')
    file_list = os.listdir(input_directory)

    files = []

    for file in file_list:
        full_path = os.path.join(input_directory, file)
        file = File(full_path)
        # print(is_valid_format(file))
        if valid_extension(file) and is_valid_format(file):
            files.append(file)
    return files


# ---------------------------------------------------------


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
        # print(file_buffer.get('TYPE'), format.get('TYPE'))
        if format.keys() == file_buffer_keys and file_buffer.get('TYPE').strip() == format.get('TYPE').strip():
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


# TODO: Implement writer functionality for docx
def file_writer(buffer, template: File):
    try:
        if template.extension == ".pdf":
            write_to_pdf(buffer, template)
        else:
            raise NotImplementedError("writing to docx is not implemented yet.")
    except Exception as e:
        raise Exception(f"{e}")


