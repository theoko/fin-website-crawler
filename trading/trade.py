"""
Trading will be based on the sentiment generated from the latest news. Since the point is that the sentiment moves
are usually close to the three major indexes (Dow Jones, S&P 500, Nasdaq 100), ETFs that track those major indexes
will be traded.

Depending on the confidence we get from the calculated sentiment, we are going to trade the ETF with the appropriate
leverage and sell on 2% profit or 2% loss or if the sentiment turns negative. We are only going to hold as long as
the sentiment is positive.
"""

import datetime as dt
import time

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.data import get_quote_yahoo

buys = []
sells = []


class Trade:
    def __init__(self, sentiment):
        self.sentiment = sentiment

    def buy_sell_hold(self):
        """
        Sentiment > 6: buy 3x (change to distance from high)
        Sentiment > 4: buy 2x
        Sentiment > 2: buy 1x
        :param sentiment:
        :return:
        """
        etfs = []
        # Check if we are holding
        if len(buys) > 0:
            for buy in buys:
                last = get_quote_yahoo(buy[0])
                if self.sentiment <= 6.0:
                    if buy[0] == 'UDOW':
                        sells.append({})
                    elif buy[0] == 'SPXL':
                        sells.append({})
                    elif buy[0] == 'TQQQ':
                        sells.append({})

        # Check sentiment to buy
        if self.sentiment > 6.0:
            etfs.append('UDOW')
            etfs.append('SPXL')
            etfs.append('TQQQ')
        elif self.sentiment > 4.0:
            etfs.append('DDM')
            etfs.append('SSO')
            etfs.append('QLD')
        elif self.sentiment > 2.0:
            etfs.append('DIA')
            etfs.append('SPY')
            etfs.append('QQQ')
        if len(etfs) == 0:
            print("No ETFs to buy")
        else:
            for etf in etfs:
                # Record last price (potential buy)
                last = get_quote_yahoo(etf)
                print("Last %s price: %f" % (etf, last['price']))
                buys.append({etf: last['price'], 'timestamp': str(time.strftime("%Y/%m/%d %H:%M:%S"))})


if __name__ == '__main__':
    style.use('ggplot')
    trade = Trade(4.5)
    trade.buy_sell_hold()
    # -------------------------
    # start = dt.datetime(2000,1,1)
    # end = dt.datetime(2019,12,31)
    # dow_df = web.DataReader('UDOW', 'yahoo', start, end)
    # print(dow_df.tail(6))
    # sp500_df = web.DataReader('SPXL', 'yahoo', start, end)
    # print(sp500_df.tail(6))
    # nasdaq_df = web.DataReader('TQQQ', 'yahoo', start, end)
    # print(nasdaq_df.tail(6))
    # -------------------------
    # 1x leverage:
    # - DIA
    # - SPY
    # - QQQ
    # dow_1x_curr = get_quote_yahoo('DIA')
    # sp500_1x_curr = get_quote_yahoo('SPY')
    # nasdaq100_1x_curr = get_quote_yahoo('QQQ')
    # 2x leverage:
    # - DDM
    # - SSO
    # - QLD
    # dow_2x_curr = get_quote_yahoo('DDM')
    # sp500_2x_curr = get_quote_yahoo('SSO')
    # nasdaq100_2x_curr = get_quote_yahoo('QLD')
    # 3x leverage:
    # - UDOW
    # - SPXL
    # - TQQQ
    # dow_3x_curr = get_quote_yahoo('UDOW')
    # sp500_3x_curr = get_quote_yahoo('SPXL')
    # nasdaq100_3x_curr = get_quote_yahoo('TQQQ')
    # print(nasdaq100_3x_curr['price'])
    const_compounds = [
        1.2890855673030313, 1.1273886511049946, 0.7915099489074098, 1.5392346747961665, -0.9004362673032805,
        3.00032392541686, 3.3268898401816864, 3.380221205438288, 1.3924729889582093, 1.1994682159441465,
        5.116000879084923, 6.614984131077104, 6.851229982993045, 6.851229982993045, 6.862970225694011,
        5.8541641077360715, 5.882834342296299, 5.440036750712646, 6.4222532456934, 6.852868202049195, 6.547623369274014,
        5.218971951759605, 5.5635407933978875, 3.968557235400799, 2.5562346581110824, 1.992393114640773,
        1.6786539136035692, 2.0512942376819643, 0.7813940208380541, 1.249307484708416, -0.038841315960802814,
        1.8099204678737921, 2.0339351969831236, 2.3877297078374644, 2.189910797260458, 1.5763993600708646,
        1.6325675381044458, 3.240195381269063, 3.14944417160009, 0.23493256817006372, 0.19799184951087126,
        0.029784950220272832, 0.25689811097690907, 0.6428763913873862, 0.9757110201195308, -2.048366232224377,
        -0.16016504767648118, 0.9042901508302414, -0.754727288577998, -1.7552596368665054, -1.320126037408322,
        -3.1502177714615907, -3.534539457124163, -4.39760726315359, -5.469894997881271, -6.270734970335449,
        -6.030006202422028, -5.990017048823751, -5.510084803907624, -4.665983477146056, -4.554254911887023,
        -5.234889457534756, -5.563746775555786, -6.595962446582209, -6.595962446582209, -7.0852214505949505,
        -7.062608655100071, -7.062608655100071, -6.463309641604267, -6.215639935931112, -5.943550948433928,
        -5.344198232699288, -7.258658606170234, -6.6528795292537275, -6.991809233814046, -8.756709581904726,
        -10.454055462697335, -10.170721648477471, -10.420139417659119, -10.479487697332374, -11.957242470852107,
        -12.642910821333873, -12.567506692051673, -12.567506692051673, -12.567506692051673, -12.01921715713555,
        -12.05696504115518, -12.05696504115518, -12.05696504115518, -12.05696504115518, -12.05696504115518,
        -12.05696504115518, -10.692316802824092, -8.36394245138687, -8.579786129884297, -8.514700723605118,
        -8.733780861401025, -7.665341127139034, -7.543380292214199, -6.281864646616006, -5.83420942120665,
        -6.860775798789643, -6.439354588118423, -7.228078127677165
    ]
    const_starting_date = '2020-04-22 11:56:58.379312'
