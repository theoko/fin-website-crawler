from classifier.classifier import Classifier
from sites.finwebscraper import FinWebScraper


class SeekingAlphaScraper(FinWebScraper):
    def run(self):
        soup = super(SeekingAlphaScraper, self).get_soup_object()
        # Gets the trending articles from seeking alpha homepage
        # trending_articles = soup.find("div", {"id": "analysis_content"})
        # headlines = trending_articles.find_all("a", {"class": "article_link"})
        # for headline in headlines:
        #     print("----")
        #     title = headline.text
        #     print("Trending articles title: %s" % (title))
        # trending_news = soup.find("ul", {"class": "top-news"})
        # headlines = trending_news.find_all("span", {"class": "title"})
        # for headline in headlines:
        #     print("----")
        #     title = headline.text
        #     print("Trending news title: %s" % (title))
        # print(soup.find_all())
        latest_articles = soup.find("section", {"class": "step_5", "id": "latest_articles"})
        headlines = latest_articles.find_all("li", {"class": "article-elem"})
        for headline in headlines:
            title = headline.find("a")
            title_text = title.text
            print("----")
            print("Latest articles title: %s" % (title_text))
            txt_classifier = Classifier(title_text)
            sentiment = txt_classifier.sentiment()
            print(sentiment)
            self.sentiment = sentiment
            self.update_avgs()  # update averages