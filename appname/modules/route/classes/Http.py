from appname.modules.route.IRoute import IRoute


class Http(IRoute):

    _requests = ['post', 'get', 'options']

    def handle(self):
        pass

    def get_command(self):
        return self._command
