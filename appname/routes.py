from appname.modules.route.classes.Http import Http
from appname.modules.route.classes.Websocket import Websocket

from appname.modules.controller.Factory import Factory as ControllerFactory
from appname.modules.middleware.Factory import Factory as MiddlewaresFactory

from appname.modules.locators.controller.classes.File import File as ControllerFile
from appname.modules.locators.middleware.classes.File import File as MiddlewareFile


controllers = ControllerFactory(ControllerFile('config.locators.file.controllers', 'controllers'))
middlewares = MiddlewaresFactory(MiddlewareFile('config.locators.file.middlewares', 'middlewares'))

routes = [
    Http('get:/api/user/test', controllers.get('User'), middlewares.get(['Auth'])),

    Websocket('authorize', controllers.get('Socket'), middlewares.get(['A', 'B']))
]