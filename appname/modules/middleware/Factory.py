from appname.modules.locators.middleware.IMiddlewareLocator import IMiddlewareLocator


class Factory:

    __locator = None

    def __init__(self, locator: IMiddlewareLocator):
        self.__locator = locator
