from appname.modules.middleware.locators.IMiddlewareLocator import IMiddlewareLocator


class Factory:

    __locator = None

    def __init__(self, locator: IMiddlewareLocator):
        self.__locator = locator
