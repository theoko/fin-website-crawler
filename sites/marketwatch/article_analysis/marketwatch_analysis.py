import yfinance
from sites.finarticle import FinArticle
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


class MarketwatchAnalysis(FinArticle):
    def get_symbols(self):
        self.text = self.response.text
        soup = BeautifulSoup(self.text, 'html.parser')
        keywords = soup.find("meta", attrs={'name': 'news_keywords'})
        content = keywords["content"].split(",")
        category = content[0]
        symbols = []
        for i in range(1, len(content)):
            symbols.append(content[i])
            # symbol = content[i].split(":")[1]
            # stock_data = yfinance.download(content[i], '2020-01-01', '2020-02-05')
            # stock_data.Close.plot()
            # plt.show()
            # print(ystockquote.get_bid_realtime(symbol))
        return symbols
