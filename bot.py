import time
import ccxt
from strategies import get_strategy

class TradingBot:
    def __init__(self, exchange_name, api_key, api_secret, use_demo, strategy, signals, max_trades, symbol, amount, stop_loss_percentage, take_profit_percentage):
        self.exchange_name = exchange_name
        self.api_key = api_key
        self.api_secret = api_secret
        self.use_demo = use_demo
        self.strategy = strategy
        self.signals = signals
        self.max_trades = max_trades
        self.symbol = symbol
        self.amount = amount
        self.stop_loss_percentage = stop_loss_percentage
        self.take_profit_percentage = take_profit_percentage
        self.exchange = self.login()

    def login(self):
        exchange_class = getattr(ccxt, self.exchange_name)
        exchange = exchange_class({
            'apiKey': self.api_key,
            'secret': self.api_secret,
        })

        if self.use_demo and hasattr(exchange, 'set_sandbox_mode'):
            exchange.set_sandbox_mode(True)

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