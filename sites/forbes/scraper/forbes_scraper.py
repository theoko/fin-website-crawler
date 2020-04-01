from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper


class ForbesScraper(FinWebScraper):
    def run(self):
        soup = super(ForbesScraper, self).get_soup_object()
        # Gets the breaking article from Forbes investing page
        headline = soup.find_all("a", {"class": "headlink h1--dense card__color--benjamins-green"})[0]
        headline_text = headline.text
        headline_link = headline.get('href', '')
        print("----")
        print("Breaking article: %s" % (headline_text))
        print("Breaking article link: %s" % (headline_link))
        txt_classifier = Classifier(headline_text)
        print(txt_classifier.sentiment())
        # Gets the editors' picks on the left side
        latest_picks = {}
        for latest_picks_article in soup.find_all("a", {"class": "section-pick__title"}):
            self.article_link, link = latest_picks_article.get('href', ''), latest_picks_article.get('href', '')
            self.article_title, title = latest_picks_article.text, latest_picks_article.text
            latest_picks[link] = title
            print("----")
            print("Latest pick link title: %s" % (title))
            print("Latest pick link: %s" % (link))
            txt_classifier = Classifier(title)
            # print("Score: %f" % (txt_classifier.sentiment()))
            sentiment = txt_classifier.sentiment()
            print(sentiment)
            self.sentiment = sentiment
            self.update_avg_compound() # update average compound
            self.save()  # save article to database
