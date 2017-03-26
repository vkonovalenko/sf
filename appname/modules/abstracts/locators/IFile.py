import importlib
from abc import ABC


class IFile(ABC):

    _file_data = {}

    def __init__(self, file_path, var_name):
        self.load_from_file(file_path, var_name)

    def load_from_file(self, file_path, var_name):
        module = importlib.import_module(file_path, var_name)
        self._file_data = getattr(module, var_name)
