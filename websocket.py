import asyncio
import json
from aiohttp.web import (Application, Response, WebSocketResponse, WSMsgType)

from appname.modules.request.classes.Websocket import Websocket
from appname.modules.locators.middleware.classes.File import File as MiddlewareFile
from appname.modules.locators.route.classes.File import File as RouteFile
from appname.modules.route.classes.Websocket import Websocket as aaaaaaa


async def wshandler(request):
    resp = WebSocketResponse()
    await resp.prepare(request)
    try:
        # if resp not in request.app['sockets']:
        request.app['sockets'].append(resp)

        async for msg in resp:
            if msg.type == WSMsgType.TEXT:

                websocket = Websocket(request)
                websocket.handle_params(msg.data)
                data = websocket.get_data()

                routes_file = RouteFile('routes.routes', 'routes')

                # .get_routes()

                # command = websocket.command()

                # 1. Локаторы хранят классы в формате ['Alias': class] (кроме модуля route)
                # 2. Каждая фабрика должна иметь экземпляр локатора, для доступа к классу по алиасу
                # 3. Элементы роута должны объявляться в виде экземпляра класса (Http либо Websocket)
                # 4. Где влепить Фасад?

                try:
                    from sockets.routes.routes import routes_map
                    command = json_data.get('command')
                    command_not_found = True
                    if type(command) is str and command:
                        for route in routes_map:
                            if command == route[0]:
                                handler = route[1](data, route=route)
                                if getattr(handler, command):
                                    command_not_found = False
                                    before_return = True
                                    if hasattr(handler, '_before'):
                                        before_return = getattr(handler, '_before')(resp)
                                    if before_return:
                                        is_async = asyncio.iscoroutinefunction(getattr(handler, command))
                                        if is_async:
                                            await getattr(handler, command)(resp)
                                        else:
                                            getattr(handler, command)(resp)
                    if command_not_found is True:
                        from sockets.handlers.BaseHandler import BaseHandler
                        handler = BaseHandler(resp)
                        handler.make_response({"command": command}, 'command_not_found', resp)
                except Exception as e:
                    handler.make_response({"error": "exception"}, str(e), resp)
            else:
                return resp
        return resp
    finally:
        # разрываем соединение
        from sockets.helpers.Socket import Socket
        Socket.update_last_connection(resp)
        Socket.del_client(resp)
        request.app['sockets'].remove(resp)
        # for ws in request.app['sockets']:
        #     ws.send_str('Someone disconnected.')


async def on_shutdown(app):
    for ws in app['sockets']:
        await ws.close()

async def init(loop):
    app = Application(loop=loop)
    app['sockets'] = []
    app.router.add_get('/', wshandler)
    app.on_shutdown.append(on_shutdown)
    return app



loop = asyncio.get_event_loop()
app = loop.run_until_complete(init(loop))
# run_app(app)