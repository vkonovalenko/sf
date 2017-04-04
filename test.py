from appname.modules.request.classes.Websocket import Websocket
from appname.modules.locators.File import File as LocatorFile


# request = 'asssdds';
# text = {'test': 'json'}

# websocket = Websocket(request)
# websocket.handle_params(text)
# data = websocket.get_data()

routes = LocatorFile('appname.routes', 'routes')
route_objects = routes.get_classes()
for route in route_objects:
    if route.get_command() == 'authorize':
        handler_class = route.get_handler()
        handler = handler_class('request')

        for middleware_class in route.get_middlewares():
            middleware = middleware_class(handler)
            middleware.handle()
