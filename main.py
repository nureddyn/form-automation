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
    # print(get_form_template_list()[0].path)
    return


if __name__ == "__main__":
    main()
