from sites.finwebscraper import FinWebScraper
from ..analysis.marketwatch_analysis import MarketwatchAnalysis


class MarketwatchScraper(FinWebScraper):
    def run(self):
        soup = super(MarketwatchScraper, self).get_soup_object()
        for article in soup.find_all(('div', {"class": "element element--article no-shade"})):
            for content in article.find_all("div", {"class": "article__content"}):
                for headline in content.find_all("h3", {"class": "article__headline"}):
                    for article_link in headline.find_all("a"):
                        link_text = article.text
                        href_attr = article_link['href']
                        if self.validate_url(href_attr, "www.marketwatch.com"):
                            # print("Title: %s" % (link_text))
                            print("Link: %s" % (href_attr))
                            # analysis = MarketwatchAnalysis(href_attr)
                            # print(analysis.get_symbols())
                            print("----")
                            return (link_text, href_attr)