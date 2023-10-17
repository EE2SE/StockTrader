import yfinance as yf
import requests


class MyStock:

    def __init__(self, ticker):
        """
        initilise the object
        :param ticker: string containing the ticker name
        """
        self.__EPS = 0

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

    def get_eps(self):
        return self.__EPS

    def __find_eps(self):
        # fetch the diluted EPS
        # EPS is the first step to calculating the P/E Ratio as a valuation metrics
        # While the basic EPS is a good measure of current profitability, the diluted EPS is more scientific
        # as it also includes potential dilutions and shareholders are not in for a very nasty surprise.
        self.__EPS = self.ticker.quarterly_income_stmt.T['Diluted EPS']


if __name__ == "__main__":
    a = MyStock("AAPL")
    print(a.get_eps())
