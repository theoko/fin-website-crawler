from stock_data.symbols import Symbol, get_ticker_list
from stock_parser.stock import StockParser
from sites.marketwatch.marketwatch import Marketwatch

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
    mw = Marketwatch(url)
    mw.get_symbols()
