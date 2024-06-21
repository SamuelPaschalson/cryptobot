def get_user_input_from_form(form):
    exchange_url = form.get("exchange_url")
    username = form.get("username")
    password = form.get("password")
    strategy = form.get("strategy")
    signals = form.get("signals").split(',')
    max_trades = int(form.get("max_trades"))
    symbol = form.get("symbol")
    amount = float(form.get("amount"))
    return exchange_url, username, password, strategy, signals, max_trades, symbol, amount