from appname.modules.request.IRequest import IRequest
from aiohttp.web import WSMsgType
import json

# @TODO: delete dependency from concrete Json format

class Websocket(IRequest):

    # here request is msg from code "async for msg in resp:" in websocket server
    def init(self):
        if self._request.type == WSMsgType.TEXT:
            try:
                data = json.loads(self._request.data)
            except:
                data = {}
            self._data = data

    def handle_params(self, params=None):
        pass

    def command(self):
        return self._data.get('command')
