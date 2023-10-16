import yfinance as yf
import requests

class MyStock:
    def __init__(self, ticker):
        # check ticker is a string

        try:
            self.ticker = yf.Ticker(ticker)
            print(self.ticker.info)

        except requests.exceptions.HTTPError as e:
            print(str(ticker) + " is an invalid ticker. " + str(e))

        except TypeError as e:
            print(str(ticker) + " is an invalid ticker. ")

if __name__ == "__main__":

    a = MyStock("qw12qw")




