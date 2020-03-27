from sites.finwebscraper import FinWebScraper


class ForbesScraper(FinWebScraper):
    def run(self):
        soup = super(ForbesScraper, self).get_soup_object()
        # Gets the breaking article from Forbes investing page
        headline = soup.find_all("a", {"class": "headlink h1--dense card__color--benjamins-green"})[0]
        headline_text = headline.text
        headline_link = headline.get('href', '')
        print("Breaking article: %s" % (headline_text))
        print("Breaking article link: %s" % (headline_link))
        # Gets the editors' picks on the left side
        latest_picks = {}
        for latest_picks_article in soup.find_all("a", {"class": "section-pick__title"}):
            link = latest_picks_article.get('href', '')
            title = latest_picks_article.text
            latest_picks[link] = title
            print("Latest pick: %s" % (link))
