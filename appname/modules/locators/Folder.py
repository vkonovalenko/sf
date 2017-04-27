import importlib
from appname.modules.locators.ILocator import ILocator


class Folder(ILocator):

    def __init__(self, folder_path):
        self._location = folder_path

    def get(self, alias):
        module = importlib.import_module(self._location + '.' + alias, alias)
        return getattr(module, alias)
