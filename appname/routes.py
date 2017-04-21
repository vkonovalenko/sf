from appname.modules.route.classes.Http import Http
from appname.modules.route.classes.Websocket import Websocket

from appname.modules.Factory import Factory
from appname.modules.locators.File import File as FileLocator


controllers = Factory(FileLocator('appname.config.locators.controllers', 'controllers'))
middlewares = Factory(FileLocator('appname.config.locators.middlewares', 'middlewares'))

routes = [
    # Http('get:/api/user/test', controllers.get('User'), middlewares.get(['Auth', 'Auth2'])),

    Websocket('test', controllers.get('User'), middlewares.get(['Auth', 'Auth2'])),
    # Websocket('authorize', controllers.get('Socket'), middlewares.get('A'))
]
