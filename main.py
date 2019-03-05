from stock_data.symbols import Symbol
from stock_parser.stock import StockParser

if __name__ == '__main__':

    # URL of article
    url = 'https://www.marketwatch.com/story/oracle-earnings-chronic-cloud-concerns-create-crisis-of-confidence-2018-12-14'

    symbols = Symbol()

    # Download symbols (NASDAQ)
    # symbols.download()

    # Will write 3 files:
    # -- nasdaqlisted.txt
    # -- otherlisted.txt
    # -- tickers.txt
    # symbols.write_file()

    tickers = symbols.get_ticker_list()

    stocks = StockParser(url, tickers)
    stocks.parse()
    print(stocks.getArticleSymbols())