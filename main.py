import datetime
import sys

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from apscheduler.schedulers.blocking import BlockingScheduler

from alexa.top_sites import TopSites
from db.database import Database
from misc.stock_data.symbols import Symbol
from sites.cnn.scraper.cnn_scraper import CnnScraper
from sites.fool.scraper.fool_scaper import FoolScraper
from sites.forbes.scraper.forbes_scraper import ForbesScraper
from sites.financial_times.scraper.ft_scraper import FinancialTimesScraper
from sites.marketwatch.scraper.marketwatch_scraper import MarketwatchScraper
from sites.seeking_alpha.scraper.seeking_alpha_scraper import SeekingAlphaScraper
from sites.the_balance.scraper.the_balance_scraper import TheBalanceScraper
from sites.vanguard.scraper.vanguard_scraper import VanguardScraper
from sites.yahoo_finance.scraper.yfinance_scraper import YFinanceScraper
from utils.average import Average
from utils.memcached import MemcachedUtils
from utils.website_average import WebsiteAverage

weighted_compounds = []
dates = []


def run_alexa_scraper():
    ## Runs the Alexa scraper
    top_sites = TopSites()
    top_sites.collect()
    print(TopSites.weights)


def run_website_scrapers():
    # TODO: fix scraper
    ## Runs the yahoo finance scraper
    # yfinance = YFinanceScraper("https://finance.yahoo.com")
    # yfinance.run()

    # TODO: fix scraper
    ## Runs the marketwatch scraper
    mw = MarketwatchScraper("https://www.marketwatch.com/")
    mw.run()
    # sys.exit("stopped execution")

    ## Runs the forbes scraper
    print("---- FORBES ----")
    forbes = ForbesScraper("https://www.forbes.com/investing/")
    forbes.run()

    ## Runs the financial times scraper
    print("---- FINANCIAL TIMES ----")
    ft = FinancialTimesScraper("https://www.ft.com/equities")
    ft.run()

    ## Runs the fool scraper
    print("---- FOOL ----")
    fool = FoolScraper("https://www.fool.com")
    fool.run()

    ## Runs the cnn scraper
    print("---- CNN Business ----")
    cnn = CnnScraper("https://money.cnn.com")
    cnn.run()

    ## Runs the balance scraper
    print("---- The balance ----")
    the_balance = TheBalanceScraper("https://www.thebalance.com")
    the_balance.run()

    # TODO: fix scraper
    ## Runs the vanguard scraper
    # print("---- Vanguard ----")
    # vanguard = VanguardScraper("https://investornews.vanguard")
    # vanguard.run()

    ## Runs the seeking alpha scraper
    # print("---- Seeking alpha ----")
    # Average.weights.append(TopSites.weights['seekingalpha.com'])
    # seeking_alpha = SeekingAlphaScraper("https://seekingalpha.com")
    # seeking_alpha.run()


def get_compound():
    """
    Print the date that the method started running
    """
    time = datetime.datetime.now()
    print("Started: %s %s" % (time.strftime("%x"), time.strftime("%X")))
    """
    Run the Alexa scraper to find out the website rankings
    """
    run_alexa_scraper()
    # sys.exit("stopped execution")

    """
    Run the scraper for each website and store both the article and the link in the database
    """
    run_website_scrapers()

    """
    Get the average compound
    """
    print("---- Average compound (not weighted) ----")
    print("average compound: %f, %f (x100)" % (Average.get_average_compound(), Average.get_average_compound() * 100.0))

    """
    Get the average negative
    """
    print("---- Average negative (not weighted) ----")
    print("average negative: %f, %f (x100)" % (Average.get_average_neg(), Average.get_average_neg() * 100.0))

    """
    Get the average neutral
    """
    print("---- Average neutral (not weighted) ----")
    print("average neutral: %f, %f (x100)" % (Average.get_average_neu(), Average.get_average_neu() * 100.0))

    """
    Get the average positive
    """
    print("---- Average positive (not weighted) ----")
    print("average positive: %f, %f (x100)" % (Average.get_average_pos(), Average.get_average_pos() * 100.0))

    """
    Get the weighted compound average
    """
    print("---- Weighted compound average ----")
    # print(WebsiteAverage.websites)
    # print(TopSites.weights)
    wa = WebsiteAverage.get_weighted_average_compound()
    print("weighted compound average based on total sites linking a site: %f, %f (x100)" % (wa, wa * 100.0))
    weighted_compounds.append(wa * 100.0)
    dates.append(datetime.datetime.now())
    print("weighted compounds are: " + ', '.join(str(x) for x in weighted_compounds))
    print("dates are: " + ', '.join(str(x) for x in dates))
    x = [
        # dt.datetime(2020, 4, 6, 9, 53),
        # dt.datetime(2020, 4, 6, 12, 11),
        # dt.datetime(2020, 4, 6, 12, 52),
    ]
    for date in dates:
        x.append(date)
    y = [
        # 5.359826,
        # -0.997296,
        # -2.628850,
    ]
    for compound in weighted_compounds:
        y.append(compound)
    fig, ax = plt.subplots()
    ax.plot_date(x, y, linestyle='-')
    fig.autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    # Debug
    # sys.exit("stopped execution")

    # URL of article
    # This is for testing purposes
    # Symbols contained in article: 
    #   - ORCL
    #   - GOOG
    #   - GOOGL
    #   - AMZN
    #   - MSFT
    #   - SAP
    #   - DJIA
    #   - SPX
    #   - COMP
    url = 'https://www.marketwatch.com/story/oracle-earnings-chronic-cloud-concerns-create-crisis-of-confidence-2018-12-14'

    symbols = Symbol()

    # Download symbols (from NASDAQ index)
    # symbols.download()

    # Will write 3 files:
    # -- nasdaqlisted.txt
    # -- otherlisted.txt
    # -- tickers.txt
    # symbols.write_file()

    # tickers = get_ticker_list()
    # stocks = StockParser(url, tickers)
    # stocks.parse()
    # print(stocks.getArticleSymbols())

    """
    Initialize database
    """

    ## Create db and necessary tables
    # db = Database()
    # db.create_tables()

    """
    Get the compound and continue for every hour
    """
    get_compound()
    scheduler = BlockingScheduler()
    scheduler.add_job(get_compound, 'interval', hours=1)
    scheduler.start()
