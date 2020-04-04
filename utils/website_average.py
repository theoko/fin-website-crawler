from urllib.parse import urlparse

import numpy as np

from alexa.top_sites import TopSites


class WebsiteAverage:
    websites = {}

    def __init__(self, url):
        self.sums = []
        self.url = url

    def add(self, val):
        self.sums.append(val)
        WebsiteAverage.websites[urlparse(self.url).netloc.replace('www.', '')] = self.get_average()

    def get_average(self):
        return np.average(self.sums)

    @staticmethod
    def get_weighted_average_compound():
        compounds = []
        weights = []
        for key, value in WebsiteAverage.websites.items():
            compounds.append(WebsiteAverage.websites[key])
            weights.append(TopSites.weights[key])
        print(compounds)
        print(weights)
        return np.average(compounds, weights=weights)
