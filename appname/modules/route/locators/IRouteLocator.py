from abc import abstractmethod
from appname.modules.abstracts.locators.ILocator import ILocator


class IRouteLocator(ILocator):

    _routes = []

    def __init__(self, data, other_data=None):
        self._load(data, other_data)

    def get_routes(self):
        return self._routes

    @abstractmethod
    def _load(self, data, other_data=None):
        pass
