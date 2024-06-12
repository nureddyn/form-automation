from .buffer import *
from .classes.File import File

def file_reader(file: File) -> Dict[str, str]:
    if file.extension == ".csv":
        return csv_buffer(file.path)
    elif file.extension == ".xlsx":
        return excel_buffer(file.path)
    elif file.extension == ".gsheet":
        return gsheet_buffer(file.path)
    elif file.extension == ".pdf":
        return pdf_buffer(file.path)
    # raise ValueError("File type not supported for reading")