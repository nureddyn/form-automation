import os
import subprocess
import platform
from .path_handling import *
from typing import List, Any, Dict
from .classes.File import File
from modules.file_formats import data_formats
from .buffer import *
from .reader import *
from .writer import *

# TODO: Create a function that fetch forms from source website and saves them in a folder called "templates"
"""
    This function may execute a script that uses 'wget' or 'curl' command
"""
def fetch_forms():
    templates_path = get_absolute_path("templates")
    
    # TODO: create a predefined list of urls
    url = "https://www.alleghenycounty.us/files/assets/county/v/1/government/health/documents/food-safety/temporary-checklist-2024.pdf"
    try:
         # Ensure the destination folder exists
        os.makedirs(templates_path, exist_ok=True)

        # Get the filename from the URL
        filename = os.path.basename(url)
        file_path = os.path.join(templates_path, filename)

        # Determine fetch command based on operating system
        system = platform.system()
        if system == "Windows":
            # Construct the url command
            command = ["curl", "-o", file_path, url]
        elif system == "Linux":
            command = ["wget", url, "-P", templates_path]
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

# TODO: Create function that scans the "templates" folder and returns a list of PDF template files
"""
Example:
form
form_templates = generate_form_templates()
print(form_templates) $[template_1, template_2, ...]
"""

def generate_form_templates() -> List[File]:
    return


# TODO: Create a function that simulates a user's selection of a file, taking the file list length, and returning a file index
# This function replaces teporarly the selected index that comes from the UI
def select_random_form_type(list_length: int) -> int:
    return

# TODO: Create a function that takes a list of template files and the index selected by the user, returning the selected file
def get_selected_file(template_list: List[File], index: int) -> File:
    return



# --------------------------- Fix This -----------------------------------------
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
        print(get_template_fields(required_template))
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
        print(is_valid_format(file))
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
        print(file_buffer.get('TYPE'), format.get('TYPE'))
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


