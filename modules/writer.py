import os
from .reader import *

def write_to_pdf(buffer: Dict[str, str], template: File):
    reader = file_reader(template).get('reader')
    
    writer = PyPDF2.PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

        fields = reader.getFields(page)
        if fields:
            for key in buffer:
                if key in fields:
                    fields[key].update({"/V": buffer[key]})
            writer.updatePageFormFieldValues(page, fields)

    # Write the final pdf form in input folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, '..', 'output', "output.pdf")
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)