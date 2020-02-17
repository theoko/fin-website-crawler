from misc.stock_data.symbols import Symbol
from sites.marketwatch.article_analysis.marketwatch_analysis import MarketwatchAnalysis
from sites.marketwatch.website_scraper.marketwatch_scraper import MarketwatchScraper

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
    #
    # stocks = StockParser(url, tickers)
    # stocks.parse()
    # print(stocks.getArticleSymbols())
    # mw = Marketwatch(url)
    # print(mw.get_symbols())
    mw = MarketwatchScraper("https://www.marketwatch.com/")
    mw.run()
