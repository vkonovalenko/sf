from abc import ABC, abstractmethod


class ILocator(ABC):

    _classes = {}

    def get_class(self, alias):
        result = self._classes.get(alias)
        if result is not None:
            return result
        else:
            raise Exception(alias + ' not found in locator.')
