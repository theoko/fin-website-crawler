from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper


class VanguardScraper(FinWebScraper):
    def run(self):
        """
        h2: post-title
        a: title
        """
        soup = super(VanguardScraper, self).get_soup_object()
        print("---- Most viewed ----")
        for headline in soup.find_all("h2", {"class": "post-title"}):
            headline_link = headline.find("a")
            span = headline_link.find("span")
            span_text = span.text
            headline_link_href = headline_link.get('href', '')
            print("----")
            print("Headline: %s" % (span_text))
            print("Article link: %s" % (headline_link_href))
            self.classify_headline(span_text)
