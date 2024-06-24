import time
import ccxt
from strategies import get_strategy

class TradingBot:
    def __init__(self, exchange_url, username, password, strategy, signals, max_trades, symbol, amount, stop_loss_percentage, take_profit_percentage):
        self.exchange_url = exchange_url
        self.username = username
        self.password = password
        self.strategy = strategy
        self.signals = signals
        self.max_trades = max_trades
        self.symbol = symbol
        self.amount = amount
        self.stop_loss_percentage = stop_loss_percentage
        self.take_profit_percentage = take_profit_percentage
        self.exchange = self.login()

    def login(self):
        exchange = ccxt.binance({
            'apiKey': self.username,
            'secret': self.password,
        })
        return exchange

    def run(self):
        strategy = get_strategy(self.strategy)
        return strategy(self)

    def execute_trade(self, side):
        order = self.exchange.create_order(
            symbol=self.symbol,
            type='market',
            side=side,
            amount=self.amount
        )
        return order