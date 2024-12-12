import pandas as pd
from yfinance import Ticker

def fetch_data(symbol, interval):
    """
    Fetches historical stock data for the given symbol using Yahoo Finance.

    Parameters:
        symbol (str): Stock ticker symbol (e.g., 'AAPL', 'TSLA').

    Returns:
        pandas.DataFrame: DataFrame containing historical stock data.
    """
    data = Ticker(symbol).history(period='1mo', interval=interval)
    return data