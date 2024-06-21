from flask import render_template, request
from app import app
from config import get_user_input_from_form
from bot import connect_to_exchange, execute_trades

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        exchange_url, username, password, strategy, signals, max_trades, symbol, amount = get_user_input_from_form(request.form)
        stop_loss_pct = float(request.form.get("stop_loss_pct"))
        take_profit_pct = float(request.form.get("take_profit_pct"))
        exchange = connect_to_exchange(exchange_url, username, password)
        execute_trades(exchange, signals, strategy, max_trades, stop_loss_pct, take_profit_pct, symbol, amount)
        return render_template("result.html", result="Trading started successfully!")
    return render_template("index.html")