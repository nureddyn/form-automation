import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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
    template_list = get_form_template_list()
    template_index = select_random_form_type(len(template_list))
    selected_file = get_selected_file(template_list, template_index)
    print(selected_file.path)
    return


if __name__ == "__main__":
    main()
