
import yfinance as yf  # Fetched the data from Yahoo Finance
import pandas as pd

def get_stock_prices(ticker, time_frame="1d", frequency="1m"):
    """Fetch stock prices for a given ticker.
    Args:
        ticker (str): Stock symbol (e.g., 'AAPL').
        time_frame (str): Period to fetch (e.g., '1d' for one day).
        frequency (str): Data interval (e.g., '1m' for one minute).
    Returns:
        pandas.DataFrame: Stock data with Close prices or None if failed."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=time_frame, interval=frequency)
        if data.empty:
            print(f"[Error] No data retrieved for {ticker}")
            return None
        return data[["Close"]]
    except Exception as e:
        print(f"[Error] Failed to fetch data for {ticker}: {e}")
        return None