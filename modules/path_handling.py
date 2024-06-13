import os

def get_absolute_path(folder_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    folder = os.path.join(project_dir, folder_name)
    if os.path.isdir(folder):
        return folder
    else:
        raise FileNotFoundError(f"'{folder_name}' folder does not exist.")
