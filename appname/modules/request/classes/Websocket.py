from modules.request.IRequest import IRequest
import json


class Websocket(IRequest):

    _json_data = {}

    def init(self):
        pass

    def handle_params(self, params=None):
        try:
            self._json_data = json.loads(params)
        except:
            pass

        data = self._json_data.get('data')
        if data is None or type(data) is not dict:
            data = {}
        self._data = data

    def command(self):
        return self._json_data.get('command')
