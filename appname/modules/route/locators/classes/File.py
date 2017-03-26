import importlib
from appname.modules.route.locators.IRouteLocator import IRouteLocator


class File(IRouteLocator):

    def _load(self, file_path, var_name):
        module = importlib.import_module(file_path, var_name)
        self._routes = getattr(module, var_name)
