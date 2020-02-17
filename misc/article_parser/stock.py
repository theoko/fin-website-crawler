from newspaper import Article
import ystockquote


class StockParser:

    def __init__(self, url, tickers_list):
        
        # Article Object
        self.article = Article(url)
        self.tickers = tickers_list
    
    def parse(self):
        self.article.download()
        self.article.parse()

        return True

    def getAuthors(self):
        return self.article.authors

    def getArticleText(self):
        return self.article.text

    def getArticleInSentences(self):

        # Article text
        # Remove empty lines
        text = self.article.text.replace('\n\n', '\n')

        # Split where dot (.) is detected
        return text.split('. ')
