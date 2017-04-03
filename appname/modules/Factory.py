from abc import ABC
from appname.modules.abstracts.locators.ILocator import ILocator


class Factory(ABC):

    __locator = None

    def __init__(self, locator: ILocator):
        self.__locator = locator

    def get(self, alias):
        return self.__locator.get_classes().get(alias)
