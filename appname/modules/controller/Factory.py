from appname.modules.locators.controller.IControllerLocator import IControllerLocator


class Factory:

    __locator = None

    def __init__(self, locator: IControllerLocator):
        self.__locator = locator
