# trading-bot-api

This is a python based API that allows automated trading by connecting TradingView and Binance.

The algorithm is written in TradingView using the pineScript language. The buy and sell orders are sent over to the python API via a webhook which contains details of the order (i.e ticker, bid, quantity, order type). The API which runs on a heroku server then pushes the information onto binance where the order is executed. 

