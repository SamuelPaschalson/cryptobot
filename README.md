# Crypto Trading Bot

## Overview

This is a simple crypto trading bot with a web interface that connects to your crypto exchange account, follows user-defined trading signals, and executes trades based on those signals.

## Setup

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd crypto_trading_bot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the web interface.

3. Fill out the form with your trading details and start trading.

## Trading Strategies

-   **Scalping:** Trades a specified number of signals after ignoring the first one.
-   **Day Trading:** Trades a specified number of signals within a day.
-   **Swing Trading:** Trades a specified number of signals based on market swings.
-   **Position Trading:** Trades a specified number of signals over a longer period.

## Disclaimer

Use this bot at your own risk. Trading cryptocurrencies involves significant risk and can result in the loss of your capital.
