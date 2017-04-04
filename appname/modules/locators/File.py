import importlib
from appname.modules.abstracts.ILocator import ILocator


class File(ILocator):

    def __init__(self, file_path, var_name):
        self._location = file_path
        self.__load_from_file(file_path, var_name)

    def __load_from_file(self, file_path, var_name):
        module = importlib.import_module(file_path, var_name)
        self._classes = getattr(module, var_name)
