import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modules.writer import *

from modules.utils import *
def main():

    # Create the list of file instances
    # TODO: Fix this:
    input_files = get_input_file_list()
    # is_valid_format(files[0])

    # Print file content:
    # print(file_reader(files[0]))
    # generate_forms(input_files)

    # fetch_forms()
    # template_list = get_file_list("templates")
    
    # check if there are files in "templates" folder
    # if len(template_list) > 0:
    #     template_index = random_index(len(template_list))
    #     selected_file = get_selected_file(template_list, template_index)
    #     # print(selected_file.path)
    #     write_to_excel(selected_file)
        
    # else:
    #     print("There aren't template files.")
    # return
    output_list = get_file_list("output")
    templates = get_file_list("templates")
    # TODO: Create a function that compares the template type with the spreadsheet type, 
    # to select a file without hardcoding the process
    template = get_selected_file(templates, 0)
    if len(output_list) > 0:
        file_index = random_index(len(output_list))
        selected_file = get_selected_file(output_list, file_index)
        print(selected_file.path)
        buffer = file_reader(selected_file)
        write_to_pdf(buffer, template)




if __name__ == "__main__":
    main()
