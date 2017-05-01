from abc import ABC, abstractmethod


class IRequest(ABC):

    _request = None
    _data = {}

    def __init__(self, request):
        self._request = request
        self.init()

    def get_data(self):
        return self._data

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def get_command(self):
        pass
