from abc import ABC, abstractmethod


class ILocator(ABC):

    _classes = {}
    _location = ''

    @abstractmethod
    def __init__(self):
        pass

    def get_classes(self):
        return self._classes

    def get_location(self):
        return self._location
