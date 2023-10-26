from stock_class import *


class AnalysedStock(MyStock):
    def __init__(self, ticker):
        super().__init__(ticker)

    # https://www.investopedia.com/day-trading/pick-stocks-intraday-trading/
    def check_volatility(self):
        # Day traders require price movement in order to make money.
        # Day traders can choose stocks that tend to move a lot, either in dollar terms or percentage terms.
        pass

    def check_liquidity(self):
        # Liquid stocks tend to have high trading volume.
        # This allows for larger quantities to be purchased and sold without significantly affecting the price.
        pass

    def check_snp_correlation(self):
        # isolate those stocks that are relatively weak or strong compared with the index
        pass
