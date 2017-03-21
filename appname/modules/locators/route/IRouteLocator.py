from abc import ABC, abstractmethod
from modules.locators.ILocator import ILocator


class IRouteLocator(ILocator):

    _routes = []

    def __init__(self, data, other_data=None):
        self._load(data, other_data)

    def get_routes(self):
        return self._routes

    @abstractmethod
    def _load(self, data, other_data=None):
        pass
