from sites.finwebscraper import FinWebScraper

class CnnScraper(FinWebScraper):
    def run(self):
        """
        cd__headline
        cd__headline-text
        :return:
        """
        soup = super(CnnScraper, self).get_soup_object()
        for headline in soup.find_all("h3", {"class": "cd__headline"}):
            for headline_text in headline.find("span", {"class": "cd__headline-text"}):
                print("Headline: %s" % (headline_text))