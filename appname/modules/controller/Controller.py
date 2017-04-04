from abc import ABC


class Controller(ABC):

    __request = None

    # aiohttp request
    def __init__(self, request):
        self.__request = request
