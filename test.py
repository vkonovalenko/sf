from appname.modules.request.classes.Websocket import Websocket
from appname.modules.locators.File import File as LocatorFile


routes = LocatorFile('appname.routes', 'routes')
route_objects = routes.get_classes()
for route in route_objects:
    # check for command from request
    # where it will be?
    if route.get_command() == 'authorize':
        handler_class = route.get_handler()
        handler = handler_class('request')

        middlewares_passed = True
        for middleware_class in route.get_middlewares():
            if middlewares_passed:
                middleware = middleware_class(handler)
                middleware.handle()
                middlewares_passed = middleware.is_passed()

        if middlewares_passed:
            handler.execute_command(route.get_command())
