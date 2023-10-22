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
        self._pe = pd.DataFrame()
        self._revenue = pd.DataFrame()
        self._peg = 0
        self._share_history = pd.DataFrame()
        self._ps = pd.DataFrame()
        self._der = pd.DataFrame()

        # try fetching the ticker
        try:
            self.ticker_name = ticker
            self.ticker = yf.Ticker(self.ticker_name)
            self.valid = True

        # if it doesn't exist HTTPError will be thrown
        except requests.exceptions.HTTPError as e:
            print(str(ticker) + " is an invalid ticker. ")
            self.valid = False

        # once we fetch it we get the info we want into our object
        else:
            self.__find_eps()
            self.__calculate_pe()
            self.__find_revenue()
            self.__calculate_peg()
            self.__find_share_history()
            self.__calculate_ps()
            self.__calculate_der()

    def get_eps(self):
        return self._eps

    def __find_eps(self):
        # fetch the diluted EPS
        # EPS is the first step to calculating the P/E Ratio as a valuation metrics
        # While the basic EPS is a good measure of current profitability, the diluted EPS is more scientific
        # as it also includes potential dilutions and shareholders are not in for a very nasty surprise.
        self._eps = 4*self.ticker.quarterly_income_stmt.T['Diluted EPS']

    def get_pe(self):
        return self._pe

    def __calculate_pe(self):
        self._pe = self._eps.copy()
        self._pe.rename("PE", inplace=True)
        # for every date in quarterly eps, get the share price
        for date in self._eps.index:
            t_start = date - timedelta(days=0, hours=0)
            t_end = date + timedelta(days=1, hours=0)
            data = self.ticker.history(interval="1d", period="5y", start=t_start, end=t_end)
            increment = 2
            while data.empty and increment < 10:
                t_start = date + timedelta(days=increment-1, hours=0)
                t_end = date + timedelta(days=increment, hours=0)
                data = self.ticker.history(interval="1d", period="5y", start=t_start, end=t_end)
                increment += 1
            if data.empty:
                print("No valid share data for ticker: " + self.ticker_name + " is available.")
            else:
                self._pe.loc[date] = data['Close'].iloc[0]/self._eps.loc[date]

    def get_revenue(self):
        return self._revenue

    def __find_revenue(self):
        self._revenue = 4*self.ticker.quarterly_income_stmt.T['Total Revenue']

    def get_peg(self):
        return self._peg

    def __calculate_peg(self):
        self._peg = self._pe.iloc[3] / (100*(1 - self._eps.iloc[3]/self._eps.iloc[0]))
        print(self._peg)

    def get_share_history_year(self):
        return self._share_history

    def __find_share_history(self):
        self._share_history = self.ticker.history(interval="1d", period="1y")

    def get_ps(self):
        return self._ps

    def __calculate_ps(self):
        # The price-to-sales ratio (Price/Sales or P/S) is calculated by taking a company's market capitalization
        # (the number of outstanding shares multiplied by the share price) and divide it by the company's total sales
        # or revenue over the past 12 months.
        market_cap = self.ticker.basic_info['marketCap']
        # last_revenue = self.ticker.financials.loc['Total Revenue'].iloc[0]
        self.__find_revenue()
        self._ps = market_cap/self.get_revenue
        pass

    def get_der(self):
        # debt equity ratio
        return self._der

    def __calculate_der(self):
        pass

if __name__ == "__main__":
    a = MyStock("TSLA")

