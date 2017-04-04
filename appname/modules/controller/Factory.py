from appname.modules.controller.locators.IControllerLocator import IControllerLocator
from appname.modules.abstracts.IFactory import IFactory


class Factory(IFactory):

    __locator = None

    def __init__(self, locator: IControllerLocator):
        self.__locator = locator

    def set_classes(self):
        pass