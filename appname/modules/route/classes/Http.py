from appname.modules.route.IRoute import IRoute


class Http(IRoute):

    __req_methods = ['post', 'get', 'options']

    def handle(self):
        pass

    def get_command(self):
        url_params = self._command.split(':')
        command = url_params[0]
        if len(url_params) == 2:
            self.__req_methods = url_params[0]
            command = url_params[1]
        self._command = command
        return self._command

    def get_methods(self):
        return self.__req_methods
