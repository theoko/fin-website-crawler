from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper


class CnnScraper(FinWebScraper):
    def run(self):
        """
        h3: cd__headline
        span: cd__headline-text
        """
        soup = super(CnnScraper, self).get_soup_object()
        for headline in soup.find_all("h3", {"class": "cd__headline"}):
            for headline_text in headline.find("span", {"class": "cd__headline-text"}):
                print("----")
                print("Headline: %s" % (headline_text))
                txt_classifier = Classifier(headline_text)
                print(txt_classifier.sentiment())
