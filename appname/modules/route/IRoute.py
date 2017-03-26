from abc import ABC, abstractmethod
from appname.modules.route.locators.IRouteLocator import IRouteLocator


class IRoute(ABC):

    _routes = []

    def __init__(self, route: IRouteLocator):
        self._routes = route.get_routes()
