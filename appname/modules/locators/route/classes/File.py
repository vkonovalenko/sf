import importlib
from appname.modules.locators.route.IRouteLocator import IRouteLocator
from appname.modules.locators.IFile import IFile


class File(IRouteLocator, IFile):

    def _load(self, file_path, var_name):
        module = importlib.import_module(file_path, var_name)
        self._routes = getattr(module, var_name)
