from appname.modules.request.classes.Websocket import Websocket
from appname.modules.route.locators.classes.File import File as RouteFile


request = 'asssdds';
text = {'test': 'json'}

websocket = Websocket(request)
websocket.handle_params(text)
data = websocket.get_data()

routes_file = RouteFile('appname.routes', 'routes')
