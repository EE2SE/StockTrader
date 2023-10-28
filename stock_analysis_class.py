from stock_class import *


class AnalysedStock(MyStock):
    def __init__(self, ticker):
        super().__init__(ticker)
        self.short_term_kpis = {"Volatility": 10.0, "Liquidity": 10000.0, "S&P Corr": 0.0}

        if self.worthy_stock:
            self.historical_data = yf.download(ticker, interval="1m", period="5d")
            self.check_volatility()
            self.check_liquidity()

        # download

    # https://www.investopedia.com/day-trading/pick-stocks-intraday-trading/
    def check_volatility(self):
        # Day traders require price movement in order to make money.
        # Day traders can choose stocks that tend to move a lot, either in dollar terms or percentage terms.
        self.volatility = self.historical_data["Close"].std()
        print(self.volatility)
        pass

    def check_liquidity(self):
        # Liquid stocks tend to have high trading volume.
        # This allows for larger quantities to be purchased and sold without significantly affecting the price.
        self.liquidity = self.historical_data["Volume"].mean()
        print(self.liquidity)
        pass

    def check_snp_correlation(self):
        # isolate those stocks that are relatively weak or strong compared with the index
        pass




if __name__ == "__main__":
    tickers = pd.read_csv("processed_tickers.csv")
    for symbol, goodstock  in zip(tickers["TICKER"],tickers["PASS"]):
        if goodstock == True:
            print(symbol)
    MSFT = AnalysedStock("MSFT")
