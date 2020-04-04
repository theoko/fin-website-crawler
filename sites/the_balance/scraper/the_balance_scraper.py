from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper


class TheBalanceScraper(FinWebScraper):
    def run(self):
        soup = super(TheBalanceScraper, self).get_soup_object()
        spotlight = soup.find("div", {"class": "homepage-spotlight__secondary"})
        article_items = spotlight.find_all("li", {"class": "card-list__item"})
        for article_item in article_items:
            link = article_item.find("a", {"class": "card-list__card"})
            title = link.find("h4", {"class": "card__title"})
            title_text = title.text
            print("----")
            print("Article title: %s" % (title_text))
            self.classify_headline(title_text)
