from appname.modules.locators.File import File as LocatorFile


routes = LocatorFile('appname.routes', 'routes')
route_objects = routes.get_classes()

# commands description
# command will be object which accepts

# parsing of the command will be realized using strategy pattern
# and it will parse params from request(must be possibility to disable it)
# it will be separate module
# name of this module "Request"
# and Http command must be compatible only with routes Http etc and maybe it's better to place them together
current_command = 'test'

for route in route_objects:
    if route.get_command() == current_command:
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
