import re

from sites.finwebscraper import FinWebScraper
from ..analysis.marketwatch_analysis import MarketwatchAnalysis


class MarketwatchScraper(FinWebScraper):
    def run(self):
        soup = super(MarketwatchScraper, self).get_soup_object()
        # print(soup.find_all())
        for article in soup.find_all(('div', {"class": "element element--article no-shade"})):
            for content in article.find_all("div", {"class": "article__content"}):
                for headline in content.find_all("h3", {"class": "article__headline"}):
                    article_link = headline.find("a")
                    link_text = re.sub(' +', ' ', article_link.text)
                    href_attr = self.remove_query_string(article_link['href'])
                    if self.validate_url(href_attr, "www.marketwatch.com"):
                        print("----")
                        print("Headline: %s" % (link_text))
                        print("Link: %s" % (href_attr))
                        self.classify_headline(link_text)
                        # analysis = MarketwatchAnalysis(href_attr)
                        # print(analysis.get_symbols())
                    # for article_link in headline.find_all("a"):
