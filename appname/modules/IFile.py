import importlib
from abc import ABC


class IFile(ABC):

    _file_data = {}

    def load_from_file(self, file_path, var_name):
        module = importlib.import_module(file_path, var_name)
        self._file_data = getattr(module, var_name)
