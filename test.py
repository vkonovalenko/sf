from appname.modules.request.classes.Websocket import Websocket
from appname.modules.locators.File import File as RouteFile


# request = 'asssdds';
# text = {'test': 'json'}

# websocket = Websocket(request)
# websocket.handle_params(text)
# data = websocket.get_data()

# list of Http or Websocket objects
routes_file = RouteFile('appname.routes', 'routes').get_classes()