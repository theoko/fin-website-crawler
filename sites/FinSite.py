from abc import ABC, abstractmethod


class FinSite(ABC):
    @abstractmethod
    def get_symbols(self): pass
