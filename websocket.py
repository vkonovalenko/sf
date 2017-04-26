#!/usr/bin/env python3
"""Example for aiohttp.web websocket server
"""

import asyncio
from aiohttp.web import (Application, Response, WebSocketResponse, WSMsgType)
from appname.modules.locators.File import File as LocatorFile
from appname.modules.request.classes.Websocket import Websocket
from aiohttp import web


async def wshandler(request):
    resp = WebSocketResponse()
    await resp.prepare(request)

    try:
        request.app['sockets'].append(resp)

        async for msg in resp:
            if msg.type == WSMsgType.TEXT:
                try:
                    req = Websocket(msg)
                    routes = LocatorFile('appname.routes', 'routes')
                    route_objects = routes.get_classes()
                    for route in route_objects:
                        if route.get_command() == req.get_command():
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
                except Exception as e:
                    handler.make_response({"error": "exception"}, str(e), resp)
            else:
                return resp
        return resp
    finally:
        #Socket.del_client(resp)
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
web.run_app(app)
