import importlib.util
import sys

"""This module defines formatting conventions for data files and form template files"""

sys.path.append('modules')

private_formats = 'private_formats'

module_spec = importlib.util.find_spec(private_formats)

if module_spec is not None:
    formats = importlib.import_module(private_formats)


    data_formats = formats.data_formats

# TODO: Look for an implementation of a default data_format
else:
    data_formats = [{}]

form_template_formats = [{}]
