# Data_cleaning.py
import pandas as pd

def clean_stock_data(data):
    """Clean and preprocess stock data.
    Args:
        data (pandas.DataFrame): Raw stock data.
    Returns:
        pandas.DataFrame: Cleaned data with moving average or None if invalid."""
    if data is None or data.empty:
        print("[Error] Invalid or empty data")
        return None
    print(f"[Debug] Raw data shape: {data.shape}")
    data = data.ffill()  
    data["Moving_Avg"] = data["Close"].rolling(window=10).mean()  
    data = data.dropna()  
    print(f"[Debug] Cleaned data shape: {data.shape}")
    return data