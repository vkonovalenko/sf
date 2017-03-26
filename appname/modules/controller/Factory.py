from appname.modules.controller.locators.IControllerLocator import IControllerLocator


class Factory:

    __locator = None

    def __init__(self, locator: IControllerLocator):
        self.__locator = locator
