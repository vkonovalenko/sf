from abc import ABC
import os, sys


class Controller(ABC):

    __status = 200
    __request = None
    __response = {}

    # aiohttp request
    def __init__(self, request):
        self.__request = request

    def execute_command(self, command):
        if hasattr(self, command):
            getattr(self, command)()
        else:
            controller_name = self.__class__.__name__;
            child_path = sys.modules[self.__class__.__module__].__file__
            raise Exception('command ' + command + ' not found in controller ' + controller_name + ': ' + child_path)

    def params(self):
        return self.__request.get_data()

    def get_response(self):
        return self.__response

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
