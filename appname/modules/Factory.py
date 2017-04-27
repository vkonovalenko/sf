from abc import ABC
from appname.modules.locators.ILocator import ILocator


class Factory(ABC):

    __locator = None

    def __init__(self, locator: ILocator):
        self.__locator = locator

    def get(self, alias):
        if type(alias) is list:
            return self.__get_many(alias)
        else:
            result = self.__locator.get(alias)
            if result is not None:
                return result
            else:
                raise Exception('alias "' + alias + '" not found in locator "' + type(self.__locator).__name__ + '" ' + self.__locator.get_location())

    def __get_many(self, aliases):
        classes = []
        for alias in aliases:
            classes.append(self.get(alias))
        return classes
