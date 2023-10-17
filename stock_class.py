import yfinance as yf
import requests
from datetime import datetime, timedelta
import pandas as pd

class MyStock:

    def __init__(self, ticker):
        """
        initilise the object
        :param ticker: string containing the ticker name
        """
        self._eps = pd.DataFrame()
        self._pe = 0

        # try fetching the ticker
        try:
            self.ticker = yf.Ticker(ticker)
            self.valid = True

        # if it doesn't exist HTTPError will be thrown
        except requests.exceptions.HTTPError as e:
            print(str(ticker) + " is an invalid ticker. ")
            self.valid = False

        # once we fetch it we get the info we want into our object
        else:
            self.__find_eps()
            self.__calculate_pe()

    def get_eps(self):
        return self._eps

    def __find_eps(self):
        # fetch the diluted EPS
        # EPS is the first step to calculating the P/E Ratio as a valuation metrics
        # While the basic EPS is a good measure of current profitability, the diluted EPS is more scientific
        # as it also includes potential dilutions and shareholders are not in for a very nasty surprise.
        self._eps = self.ticker.quarterly_income_stmt.T['Diluted EPS']

    def get_pe(self):
        return self._pe

    def __calculate_pe(self):
        # for every date in quarterly eps, get the share price
        for date in self._eps.index:
            t_start = date - timedelta(days=0, hours=0)
            t_end = date + timedelta(days=1, hours=0)
            data = self.ticker.history(interval="1d", period="5y", start=t_start, end=t_end)
            increment = 2
            while data.empty:
                t_start = date + timedelta(days=increment-1, hours=0)
                t_end = date + timedelta(days=increment, hours=0)
                data = self.ticker.history(interval="1d", period="5y", start=t_start, end=t_end)
                increment += 1

            print(data)


if __name__ == "__main__":
    a = MyStock("AAPL")

