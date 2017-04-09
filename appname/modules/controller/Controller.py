from abc import ABC


class Controller(ABC):

    __request = None

    # aiohttp request
    def __init__(self, request):
        self.__request = request

    def execute_command(self, command):
        if hasattr(self, command):
            getattr(self, command)()
        else:
            raise Exception('command ' + command + ' not found in controller.')
