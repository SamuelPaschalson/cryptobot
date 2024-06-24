def scalping_strategy(bot):
    trades_executed = 0
    for signal in bot.signals[1:]:  # Skip the first signal
        if trades_executed >= bot.max_trades:
            break
        bot.execute_trade(signal)
        trades_executed += 1
        time.sleep(1)
    return f'Scalping strategy executed {trades_executed} trades.'

def day_trading_strategy(bot):
    trades_executed = 0
    for signal in bot.signals:
        if trades_executed >= bot.max_trades:
            break
        bot.execute_trade(signal)
        trades_executed += 1
        time.sleep(1)
    return f'Day trading strategy executed {trades_executed} trades.'

def swing_trading_strategy(bot):
    trades_executed = 0
    for signal in bot.signals:
        if trades_executed >= bot.max_trades:
            break
        bot.execute_trade(signal)
        trades_executed += 1
        time.sleep(1)
    return f'Swing trading strategy executed {trades_executed} trades.'

def position_trading_strategy(bot):
    trades_executed = 0
    for signal in bot.signals:
        if trades_executed >= bot.max_trades:
            break
        bot.execute_trade(signal)
        trades_executed += 1
        time.sleep(1)
    return f'Position trading strategy executed {trades_executed} trades.'

def get_strategy(name):
    if name == 'scalping':
        return scalping_strategy
    elif name == 'day':
        return day_trading_strategy
    elif name == 'swing':
        return swing_trading_strategy
    elif name == 'position':
        return position_trading_strategy
    else:
        raise ValueError('Invalid strategy name')