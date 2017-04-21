from appname.modules.request.IRequest import IRequest
import json

# @TODO: delete dependency from concrete Json format

class Websocket(IRequest):

    def init(self):
        pass

    def handle_params(self, params=None):
        try:
            self._data = json.loads(params)
        except:
            pass

        data = self._data.get('data')
        if data is None or type(data) is not dict:
            data = {}
        self._data = data

    def command(self):
        return self._data.get('command')
