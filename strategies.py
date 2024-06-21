import time

def trade_signal_with_stop_loss(exchange, symbol, signal, trade_type, stop_loss_pct, take_profit_pct, amount):
    order_book = exchange.fetch_order_book(symbol)
    price = order_book['bids'][0][0] if trade_type == 'buy' else order_book['asks'][0][0]

    if trade_type == 'buy':
        order = exchange.create_market_buy_order(symbol, amount)
        stop_loss_price = price * (1 - stop_loss_pct / 100)
        take_profit_price = price * (1 + take_profit_pct / 100)
    else:
        order = exchange.create_market_sell_order(symbol, amount)
        stop_loss_price = price * (1 + stop_loss_pct / 100)
        take_profit_price = price * (1 - take_profit_pct / 100)
    
    print(f"Placed a {trade_type} order for {amount} {symbol} at {price}")

    while True:
        current_price = exchange.fetch_ticker(symbol)['last']
        if trade_type == 'buy':
            if current_price <= stop_loss_price or current_price >= take_profit_price:
                exchange.create_market_sell_order(symbol, amount)
                break
        else:
            if current_price >= stop_loss_price or current_price <= take_profit_price:
                exchange.create_market_buy_order(symbol, amount)
                break

        time.sleep(1)  # Adjust as needed for your strategy

def scalping_strategy(exchange, symbol, signals, max_trades, stop_loss_pct, take_profit_pct, amount):
    signals = signals[1:max_trades + 1]
    for signal in signals:
        trade_type = 'buy' if signal == 'buy' else 'sell'
        trade_signal_with_stop_loss(exchange, symbol, signal, trade_type, stop_loss_pct, take_profit_pct, amount)

def day_trading_strategy(exchange, symbol, signals, max_trades, stop_loss_pct, take_profit_pct, amount):
    for signal in signals[:max_trades]:
        trade_type = 'buy' if signal == 'buy' else 'sell'
        trade_signal_with_stop_loss(exchange, symbol, signal, trade_type, stop_loss_pct, take_profit_pct, amount)

def swing_trading_strategy(exchange, symbol, signals, max_trades, stop_loss_pct, take_profit_pct, amount):
    for signal in signals[:max_trades]:
        trade_type = 'buy' if signal == 'buy' else 'sell'
        trade_signal_with_stop_loss(exchange, symbol, signal, trade_type, stop_loss_pct, take_profit_pct, amount)

def position_trading_strategy(exchange, symbol, signals, max_trades, stop_loss_pct, take_profit_pct, amount):
    for signal in signals[:max_trades]:
        trade_type = 'buy' if signal == 'buy' else 'sell'
        trade_signal_with_stop_loss(exchange, symbol, signal, trade_type, stop_loss_pct, take_profit_pct, amount)