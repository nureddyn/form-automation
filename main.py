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

    # Handler: "Generate Spreadsheet with form fields" -> "use existing form"
    if args.command == 'spreadsheet-from-existing-form':
        if len(args.args) != 2:
            # TODO: Create a model to structure commands messages
            print(f"{args.command} requires exactly two arguments: department and form name")
        else:
            department = args.args[0]
            form_name = args.args[1]
            form_file = get_form_file(department, form_name)
            if form_file:
                write_to_excel(form_file)
            else:
                print("The form file does not exist")

    # Handler: "Generate Spreadsheet with form fields" -> "Fetch form from website"
    if args.command == 'spreadsheet-from-website-form':
        if len(args.args) != 2:
            # TODO: Create a model to structure commands messages
            print(f"{args.command} requires exactly two arguments: department and form name")
        else:
            department = args.args[0]
            form_name = args.args[1] 
            fetch_form(department, form_name)
            form_file = get_form_file(department, form_name)
            if form_file:
                write_to_excel(form_file)



if __name__ == "__main__":
    main()
