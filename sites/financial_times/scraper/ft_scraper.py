from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper


class FinancialTimesScraper(FinWebScraper):
    def run(self):
        soup = super(FinancialTimesScraper, self).get_soup_object()
        # Get articles in the Equities section
        for headline in soup.find_all("a", {"class": "js-teaser-heading-link"}):
            headline_text = headline.text
            print("----")
            print("Headline: %s" %(headline_text))
            txt_classifier = Classifier(headline_text)
            sentiment = txt_classifier.sentiment()
            print(sentiment)
            self.sentiment = sentiment
            self.update_avgs()
