import os
import sys
import argparse
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modules.writer import *

from modules.utils import *
def main():

    """
        Create a command line interface, to serve as the demo
    """
    # Create the main command and its arguments structure
    parser = argparse.ArgumentParser(description="form automation demo")
    parser.add_argument('command', type=str, help='fetch the specified form from webpage')
    parser.add_argument('args', nargs='*', help='The name of the form')
    args = parser.parse_args()


    # fetch form from website
    if args.command == 'fetch-form':
        if len(args.args) != 2:
            # TODO: Create a model to structure commands messages
            print(f"{args.command} requires exactly two arguments: department and form name")
        else:
            department = args.args[0]
            form_name = args.args[1] 
            fetch_form(department, form_name)


    # generate spreadsheet from existing form
    if args.command == 'get-fillable-spreadsheet':
        if len(args.args) != 2:
            print(f"{args.command} requires exactly two arguments: department and form name")
        else:
            department = args.args[0]
            form_name = args.args[1]
            form_file = get_form_file(department, form_name)
            if form_file:
                write_to_excel(form_file)
            else:
                print("The form file does not exist")


    # fill out form based on a spreadsheet
    if args.command == 'fill-out-form':
        if len(args.args) != 2:
            print(f"{args.command} requires exactly two argument: department and form name")
        else:
            department = args.args[0]
            form_name = args.args[1]
            spreadsheet_file = get_spreadsheet_file(department, form_name)

            if spreadsheet_file:
                print(spreadsheet_file.path)
                buffer = file_reader(spreadsheet_file)
                template = get_form_file(department, form_name)
                write_to_pdf(buffer, template)
            else:
                print("The form file does not exist")

if __name__ == "__main__":
    main()
