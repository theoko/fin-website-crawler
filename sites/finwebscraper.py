from abc import ABC
from urllib.parse import urlparse

import furl as furl
import requests
from bs4 import BeautifulSoup

from classifier.classifier import Classifier
from db.database import Database
from utils.average import Average
from utils.website_average import WebsiteAverage


# An abstract class representing a finance website scraper
class FinWebScraper(ABC):
    def __init__(self, url):
        self.response = requests.get(url)
        self.website_average = WebsiteAverage(url)

    def get_soup_object(self):
        ## Debug
        ## print("HTML: %s" % (self.response.text))
        soup = BeautifulSoup(self.response.text, "html.parser")
        return soup

    def validate_url(self, url, valid_host):
        o = urlparse(url)
        return valid_host == o.netloc

    def remove_query_string(self, url):
        return furl.furl(url).remove(args=True, fragment=True).url

    def classify_headline(self, headline):
        # Set self.sentiment
        txt_classifier = Classifier(headline)
        sentiment = txt_classifier.sentiment()
        print(sentiment)
        self.sentiment = sentiment
        self.update_avgs()

    def update_avgs(self):
        # We want to avoid neutral articles
        if self.sentiment['neu'] < 1.0:
            Average.add_compound(self.sentiment['compound'])
            Average.add_neg(self.sentiment['neg'])
            Average.add_neu(self.sentiment['neu'])
            Average.add_pos(self.sentiment['pos'])
            self.website_average.add(self.sentiment['compound'])

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
