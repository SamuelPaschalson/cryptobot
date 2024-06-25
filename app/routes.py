from flask import Blueprint, render_template, request
from bot import TradingBot

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        exchange_name = request.form['exchange_name']
        api_key = request.form['api_key']
        api_secret = request.form['api_secret']
        use_demo = request.form.get('use_demo', 'off') == 'on'
        strategy = request.form['strategy']
        signals = request.form['signals'].split(',')
        max_trades = int(request.form['max_trades'])
        symbol = request.form['symbol']
        amount = float(request.form['amount'])
        stop_loss_percentage = float(request.form['stop_loss_percentage'])
        take_profit_percentage = float(request.form['take_profit_percentage'])
        
        bot = TradingBot(
            exchange_name=exchange_name,
            api_key=api_key,
            api_secret=api_secret,
            use_demo=use_demo,
            strategy=strategy,
            signals=signals,
            max_trades=max_trades,
            symbol=symbol,
            amount=amount,
            stop_loss_percentage=stop_loss_percentage,
            take_profit_percentage=take_profit_percentage
        )
        
        result = bot.run()
        return render_template('result.html', result=result)
    
    return render_template('index.html')
