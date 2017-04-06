from abc import ABC, abstractmethod

from appname.modules import middleware
from appname.modules.locators.ILocator import ILocator
from appname.modules.controller.Controller import Controller


class IRoute(ABC):

    _command = None
    _handler = None
    _middlewares = []

    def __init__(self, command, handler: Controller, middlewares):
        self._command = command
        self._handler = handler
        if middlewares:
            self._middlewares = middlewares

    # it must parse command and execute handler action
    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def get_command(self):
        pass

    def get_middlewares(self):
        return self._middlewares

    def get_handler(self):
        return self._handler
