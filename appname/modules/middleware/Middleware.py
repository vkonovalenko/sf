from abc import ABC, abstractmethod
from appname.modules.controller.Controller import Controller


class Middleware(ABC):

    __passed = True
    _handler = None

    def __init__(self, handler: Controller):
        self._handler = Controller

    def get_handler(self):
        return self._handler

    @abstractmethod
    def handle(self):
        pass

    def set_passed(self):
        self.__passed = True

    def set_failed(self):
        self.__passed = False

    def is_passed(self):
        return self.__passed
