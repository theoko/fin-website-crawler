import requests
from bs4 import BeautifulSoup


class TopSites:
    def __init__(self):
        self.url = "https://www.alexa.com/topsites/category/Top/Business/Investing"

    def collect(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        for site_listing in soup.find_all("div", {"class": "site-listing"}):
            print(site_listing.text)
