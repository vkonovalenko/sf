from abc import ABC, abstractmethod
from appname.modules.controller.Controller import Controller


class Middleware(ABC):

    _handler = None

    def __init__(self, handler: Controller):
        self._handler = Controller

    def get_handler(self):
        return self._handler

    @abstractmethod
    def handle(self):
        pass
