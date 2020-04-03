from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper
from utils.parse import ParseUtils


class CnnScraper(FinWebScraper):
    def run(self):
        """
        h3: cd__headline
        span: cd__headline-text

        Note: it doesn't work for all the headlines
        """
        soup = super(CnnScraper, self).get_soup_object()
        for headline in soup.find_all("h3", {"class": "cd__headline"}):
            for inner_headline in headline.find("span", {"class": "cd__headline-text"}):
                print("----")
                inner_headline_text = ParseUtils.strip_tags(str(inner_headline))
                print("Headline: %s" % (inner_headline_text))
                txt_classifier = Classifier(inner_headline_text)
                sentiment = txt_classifier.sentiment()
                print(sentiment)
                self.sentiment = sentiment
                self.update_avgs()
