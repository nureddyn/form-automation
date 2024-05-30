from typing import List, Any, Dict
from .classes import File
import csv
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
import xlrd
import PyPDF2

"""
Validate file according to process of transport data from a spreadsheet to word/pdf
"""

def validate_file(file: File) -> bool:
    if file.extension in [".csv", ".xlsx", ".gsheet", ".pdf"]:
        return True
    raise ValueError("File extension not allowed")


def get_file_type(file: File) -> str:
    if file.extension in [".csv", ".xlsx", ".gsheet"]:
        return 'Input file'
    elif file.extension in [".docx", ".pdf"]:
        return 'Output file'
    raise ValueError("File type not allowed")


def file_reader(file: File) -> List[List[str]]:
    if file.extension == ".csv":
        return csv_buffer(file.path)
    elif file.extension == ".xlsx":
        return excel_buffer(file.path)
    elif file.extension == ".gsheet":
        return gsheet_buffer(file.path)
    raise ValueError("File type not supported for reading")


# TODO: Implement writer functionality for docx
def file_writer(buffer, template: File):
    if template.path == ".pdf":
        write_to_pdf(buffer, template)
    else:
        raise NotImplementedError("writing to docx or gsheet is not implemented yet.")


# TODO: Check if the following function is correct
def write_to_pdf(buffer, template: File):
    with open(template.path, "rb") as existing_file:
        reader = PyPDF2.PdfFileReader(existing_file)
        writer = PyPDF2.PdfFileWriter()

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            writer.addPage(page)

            fields = reader.getFields(page)
            if fields:
                for key in buffer:
                    if key in fields:
                        fields[key].update({"/V": buffer[key]})
                writer.updatePageFormFieldValues(page, fields)

        with open("output.pdf", "wb") as output_file:
            writer.write(output_file)
        

def csv_buffer(path: str) -> Dict[str, str]:
    buffer = {}
    column_number = 2
    try:
        with open(path, 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            # Skip the first row (Assuming the first row contains only the form type)
            next(reader)
            for row in reader:
                if len(row) == column_number:
                    buffer[row[0].strip()] = row[1].strip()

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at {path} was not found.")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied for the file at {path}.")
    except csv.Error as e:
        raise csv.Error(f"Error: An error occurred while reading the CSV file at {path}: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

    return buffer


def excel_buffer(path) -> Dict[str, str]:
    buffer = {}
    try:
        workbook = load_workbook(path, data_only=True)
        sheet = workbook.active

        # Assuming the first row contains only the form type (permanent permit, temporal permit, etc.)
        num_rows_to_skip = 1
        for row in sheet.iter_rows(min_row=num_rows_to_skip + 1, values_only=True):
            #TODO: fix this (buffer is a dict)
            buffer.append(row)
        return buffer
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at {path} was not found.")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied for the file at {path}.")
    except InvalidFileException:
        raise InvalidFileException(f"Error: The file at {path} is not a valid Excel file.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
    

def gsheet_buffer(url) -> List[List[Any]]:
    # TODO: Apply google sheets logic (configure api and get url params)
    raise NotImplementedError("Google Sheets buffer reading is not implemented yet.")
