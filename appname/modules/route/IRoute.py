from abc import ABC, abstractmethod

from appname.modules import middleware
from appname.modules.route.locators.IRouteLocator import IRouteLocator


class IRoute(ABC):

    _command = None
    _handler = None
    _middlewares = []

    def __init__(self, command, handler: IRouteLocator, middlewares):
        self._command = command
        self._handler = handler
        if middlewares:
            self._middlewares = middlewares

    # it must parse command and execute handler action
    @abstractmethod
    def handle(self):
        pass
