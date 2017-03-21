from modules.route.classes.Http import Http
from modules.route.classes.Websocket import Websocket

from modules.controller.Factory import Factory as ControllerFactory
from modules.middleware.Factory import Factory as MiddlewaresFactory

from modules.locators.controller.classes.File import File as ControllerFile
from modules.locators.middleware.classes.File import File as MiddlewareFile


controllers = ControllerFactory(ControllerFile('config.controllers', 'classes'))
middlewares = MiddlewaresFactory(MiddlewareFile('config.middlewares', 'classes'))

test = [
    Http('post|get:/api/user/profile', controllers.get('User'), middlewares.get(['Auth', 'Admin'])),

    Websocket('authorize', controllers.get('Socket'), middlewares.get(['A', 'B']))
]