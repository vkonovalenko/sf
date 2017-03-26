from appname.modules.route.classes.Http import Http
from appname.modules.route.classes.Websocket import Websocket

from appname.modules.controller.Factory import Factory as ControllerFactory
from appname.modules.middleware.Factory import Factory as MiddlewaresFactory

from appname.modules.controller.locators.classes.File import File as ControllerFile
from appname.modules.middleware.locators.classes.File import File as MiddlewareFile


controllers = ControllerFactory(ControllerFile('appname.config.locators.file.controllers', 'controllers'))
middlewares = MiddlewaresFactory(MiddlewareFile('appname.config.locators.file.middlewares', 'middlewares'))

routes = [
    Http('get:/api/user/test', controllers.get('User'), middlewares.get(['Auth'])),

    Websocket('authorize', controllers.get('Socket'), middlewares.get(['A', 'B']))
]
