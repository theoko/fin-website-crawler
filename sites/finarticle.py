from abc import ABC, abstractmethod
import requests


# An abstract class representing a finance article
class FinArticle(ABC):
    def __init__(self, url):
        self.response = requests.get(url)

    @abstractmethod
    def get_symbols(self): pass
