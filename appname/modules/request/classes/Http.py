from modules.request.IRequest import IRequest
from urllib.parse import urlparse, parse_qsl


class Http(IRequest):

    get_params = {}
    post_params = {}
    json_data = {}

    def init(self):
        pass

    def handle_params(self, params=None):
        # remove hash from url
        url = str(self._request.rel_url).replace('#', '')
        url_params = url.split('?')
        get_params = {}
        # if we have get params
        if len(url_params) > 1:
            # cut get params from main route
            url = url_params[0]
            # get string of get params
            parsed_url = urlparse(url_params[1])
            # convert get params from string to dictionary
            get_params = parse_qsl(parsed_url.path)
        self._data = url
        self.get_params = get_params

    async def set_params_async(self):
        try:
            self.post_params = await self._request.post()
        except:
            pass
        try:
            self.json_data = await self._request.json()
        except:
            pass
