import importlib
from appname.modules.locators.ILocator import ILocator


class IFile(ILocator):

    _file_data = {}

    def load_from_file(self, file_path, var_name):
        module = importlib.import_module(file_path, var_name)
        self._file_data = getattr(module, var_name)
