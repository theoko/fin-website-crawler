from sites.finarticle import FinArticle
from bs4 import BeautifulSoup


class Marketwatch(FinArticle):
    def get_symbols(self):
        print(self.response.text)