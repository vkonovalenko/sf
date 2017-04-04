from appname.modules.route.IRoute import IRoute


class Websocket(IRoute):

    def handle(self):
        pass

    def get_command(self):
        return self._command
