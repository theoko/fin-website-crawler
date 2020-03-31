from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
#from vaderSentiment import SentimentIntensityAnalyzer


# List of all available data sets: http://www.nltk.org/nltk_data/
# This explains naive bayes: http://www.nltk.org/book/ch06.html#ref-err-analysis-train
class Classifier:
    def __init__(self, sentence):
        self.sentence = sentence
        self.analyzer = SentimentIntensityAnalyzer()

    def sentiment(self):
        """
        Return a float for sentiment strength based on the input text.
        Positive values are positive valence, negative value are negative
        valence.
        """
        return self.analyzer.polarity_scores(self.sentence)
