from appname.modules.request.IRequest import IRequest
import json

# @TODO: delete dependency from concrete Json format

class Websocket(IRequest):

    # here request is msg from code "async for msg in resp:" in websocket server
    def init(self):
        try:
            data = json.loads(self._request.data)
        except:
            data = {}
        self._data = data

    def get_command(self):
        return self._data.get('command')
