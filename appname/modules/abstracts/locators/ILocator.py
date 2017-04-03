from abc import ABC, abstractmethod


class ILocator(ABC):

    _classes = {}

    @abstractmethod
    def __init(self):
        pass

    def get_classes(self):
        return self._classes
