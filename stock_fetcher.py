# stock_fetcher.py
# Custom module to fetch stock prices for Techsophy placement project

import yfinance as yf
import pandas as pd

def get_stock_prices(ticker, time_frame="1d", frequency="1m"):
    """
    Fetch minute-by-minute stock prices from Yahoo Finance.
    Args:
        ticker (str): Stock symbol (e.g., 'TSLA').
        time_frame (str): Data period (e.g., '2d' for five days).
        frequency (str): Data interval (e.g., '1m' for one minute).
    Returns:
        pandas.DataFrame: Data with Close prices or None if error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=time_frame, interval=frequency)
        if data.empty:
            print(f"[ERROR] No data found for {ticker}")
            return None
        print(f"[Debug] Fetched data for {ticker}: {data.shape} rows")
        return data[["Close"]]
    except Exception as e:
        print(f"[ERROR] Failed to fetch {ticker}: {e}")
        return None