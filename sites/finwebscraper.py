from abc import ABC
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from db.database import Database
from utils.average import Average


# An abstract class representing a finance website scraper
from utils.parse import ParseUtils


class FinWebScraper(ABC):
    def __init__(self, url):
        self.response = requests.get(url)

    def get_soup_object(self):
        ## Debug
        ## print("HTML: %s" % (self.response.text))
        soup = BeautifulSoup(self.response.text, "html.parser")
        return soup

    def validate_url(self, url, valid_host):
        o = urlparse(url)
        return valid_host == o.netloc

    def update_avgs(self):
        # We want to avoid neutral articles
        if self.sentiment['neu'] < 1.0:
            Average.add_compound(self.sentiment['compound'])
            Average.add_neg(self.sentiment['neg'])
            Average.add_neu(self.sentiment['neu'])
            Average.add_pos(self.sentiment['pos'])

    def save(self):
        db = Database()
        db.insert_article({
            'link': self.article_link,
            'title': self.article_title,
            'neg': self.sentiment['neg'],
            'neu': self.sentiment['neu'],
            'pos': self.sentiment['pos'],
            'compound': self.sentiment['compound']
        })
