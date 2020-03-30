from misc.stock_data.symbols import Symbol
from sites.marketwatch.website_scraper.cnn_scraper import CnnScraper
from sites.marketwatch.website_scraper.fool_scaper import FoolScraper
from sites.marketwatch.website_scraper.forbes_scraper import ForbesScraper
from sites.marketwatch.website_scraper.ft_scraper import FinancialTimesScraper
from sites.marketwatch.website_scraper.marketwatch_scraper import MarketwatchScraper
from sites.marketwatch.website_scraper.vanguard import VanguardScraper

if __name__ == '__main__':

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

    ## Runs the marketwatch scraper
    mw = MarketwatchScraper("https://www.marketwatch.com/")
    mw.run()

    ## Runs the forbes scraper
    # forbes = ForbesScraper("https://www.forbes.com/investing/")
    # forbes.run()

    ## Runs the financial times scraper
    # ft = FinancialTimesScraper("https://www.ft.com/equities")
    # ft.run()

    ## Runs the fool scraper
    # fool = FoolScraper("https://www.fool.com")
    # fool.run()

    ## Runs the cnn scraper
    # cnn = CnnScraper("https://www.cnn.com/business")
    # cnn.run()

    ## Runs the vanguard scraper
    # vanguard = VanguardScraper("https://investornews.vanguard")
    # vanguard.run()