from modules.utils import *

def main():

    # Create the list of file instances
    input_files = get_input_file_list()
    # is_valid_format(files[0])

    # Print file content:
    # print(file_reader(files[0]))
    generate_forms(input_files)



if __name__ == "__main__":
    main()
