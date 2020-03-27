from sites.finwebscraper import FinWebScraper


class FoolScraper(FinWebScraper):
    def run(self):
        soup = super(FoolScraper, self).get_soup_object()
        # Get trending articles
        articles_ul = soup.find("ul", {"class": "hp-trending-articles-list"})
        for article_li in articles_ul.find_all("li"):
            article = article_li.find("a")
            article_url = article.get('href', '')
            article_title = article.text
            print("Article title: %s" % (article_title))