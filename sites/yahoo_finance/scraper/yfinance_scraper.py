from sites.finwebscraper import FinWebScraper


class YFinanceScraper(FinWebScraper):
    def run(self):
        soup = super(YFinanceScraper, self).get_soup_object()
        search = soup.find_all('h1', {
            'class': 'Lh(36px) Fz(25px)--sm Fz(32px) Mb(17px)--sm Mb(20px) Mb(30px)--lg Ff($ff-primary) Lts($lspacing-md) Fw($fweight) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) Wow(bw)'})
        for headline in search:
            print(headline.text)