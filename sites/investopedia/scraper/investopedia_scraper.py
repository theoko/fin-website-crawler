from sites.finwebscraper import FinWebScraper


class InvestopediaScraper(FinWebScraper):
    def run(self):
        soup = super(InvestopediaScraper, self).get_soup_object()
        print(soup.find_all())