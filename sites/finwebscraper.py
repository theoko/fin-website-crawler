from abc import ABC
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# An abstract class representing a finance website scraper
class FinWebScraper(ABC):
    def __init__(self, url):
        self.response = requests.get(url)

    def get_soup_object(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        return soup

    def validate_url(self, url, valid_host):
        o = urlparse(url)
        return valid_host == o.netloc
