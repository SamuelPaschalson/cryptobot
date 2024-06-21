import ccxt
from strategies import scalping_strategy, day_trading_strategy, swing_trading_strategy, position_trading_strategy

def connect_to_exchange(exchange_url, username, password):
    exchange_id = exchange_url.split('//')[1].split('.')[0]
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'uid': username,
        'password': password,
    })
    return exchange

def execute_trades(exchange, signals, strategy, max_trades, stop_loss_pct, take_profit_pct, symbol, amount):
    strategy_function = {
        'scalping': scalping_strategy,
        'day': day_trading_strategy,
        'swing': swing_trading_strategy,
        'position': position_trading_strategy,
    }.get(strategy, scalping_strategy)
    
    strategy_function(exchange, symbol, signals, max_trades, stop_loss_pct, take_profit_pct, amount)