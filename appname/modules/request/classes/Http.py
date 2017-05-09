import asyncio
from appname.modules.request.IRequest import IRequest
from urllib.parse import urlparse, parse_qsl


class Http(IRequest):

    __url = None
    __parse_params = True
    __command = None
    __req_methods = None
    __action = None

    get_params = {}
    post_params = {}
    json_data = {}

    def init(self):
        self.__url = str(self._request.rel_url)
        self.__set_get_params()
        self.__parse_url()

    def __set_get_params(self):
        url = self.__url
        url_params = url.split('?')
        get_params = {}
        # if we have get params
        if len(url_params) > 1:
            # get string of get params
            parsed_url = urlparse(url_params[1])
            # convert get params from string to dictionary
            get_params = parse_qsl(parsed_url.path)
        self.get_params = get_params

    def get_url(self):
        return self.__url

    def __parse_url(self):
        url_params = self.__url.split(':')
        command = url_params[0]
        if len(url_params) == 2:
            self.__req_methods = url_params[0]
            command = url_params[1]
        self.__command = command
        self.__action = command.split('/').pop()

    async def set_params_async(self):
        try:
            self.post_params, self.json_data = await asyncio.gather(
                self._request.post(),
                self._request.json()
            )
            #@TODO: fix it
            self._data = self.post_params
            # self.post_params = await self._request.post()
        except:
            pass

    def get_command(self):
        return self.__command

    def get_action(self):
        return self.__action

    def allowed_methods(self):
        return self.__req_methods

    def not_parse_params(self):
        self.__parse_params = False
