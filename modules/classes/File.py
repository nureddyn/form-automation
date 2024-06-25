import os

class File:
    def __init__(self, path):
        self.path = path
        self.extension = self.get_extension(path)
        self.name = self.get_name(path)

    # path getter, to return the path property of an instance
    @property
    def path(self):
        return self._path

    # path setter, to construct the path property of an instance
    @path.setter
    def path(self, path):
        self.is_valid_path(path)
        self._path = path

    
    @staticmethod
    def is_valid_path(path):
        if not path:
            raise NameError("Failed to provide valid path")
        if not os.path.exists(path):
            raise FileNotFoundError(f"The path {path} does not exist")
        if not os.path.isfile(path):
            raise ValueError(f"The path '{path}' is not a file")
        

    @staticmethod
    def get_extension(path):
        _, ext = os.path.splitext(path)
        return ext.lower()

    def get_name(self, path):
        base_name = os.path.basename(path)
        name, _ = os.path.splitext(base_name)
        return name