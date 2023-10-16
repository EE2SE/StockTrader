# First Project - StockTrader

## First Objectives:
-  Somehow identify promising stocks, provide info, benchmarks, graphical data to support it
-  Pull live daily data of the current stock market. Focus on US listed stocks for timing reasons.
-  Issue Buy/Hold/Sell commands
-  Store portfolio data
-  Run backend first on Python and consider speed up later on
-  Some kind of sentiment analysis eventually?
-  Possible to link it to real trader?

## More Meat

#### Somehow identify promising stocks, provide info, benchmarks, graphical data to support it
This can be done two ways:
1. Either we start by tracking a predefined list of stocks and only analysing those and trading those.

2. Or we go head first, and find a way to pull some news/sentiment information and then analyse those stocks in the hope of finding some big movers. This would come in two stages. First - **fundamental analysis**:

	i. Compute EPS for all stocks. Access historic financial reports and calculate yearly EPS.

	ii. Track down financial statements - revenue based

	iii. Price-to-earning ratio

	iv. Price-Earnings-Growth (PEG) Ratio

	v. Price-to-Sales Ratio (P/S)

	vi. Debt-Equity Ratio


Fundamental analysis requires some KPIs. We can achieve that by setting some hardcoded values. Or somehow *learning* what a good set of parameters would look like. -> small statistics/ML problem: would require some curated set of data for training and validation. (Next level stuff for now). Will keep it more basic first to get bare bones working.

This concludes picking stocks to begin trading that day. Let's start with that.