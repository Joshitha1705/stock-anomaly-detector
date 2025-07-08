# data_cleaner.py
# Custom module to clean and preprocess stock data

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
    data = data.fillna(method="ffill") #removing the missing values
    data["Moving_Avg"] = data["Close"].rolling(window=10).mean() # for calculating the anomalies
    data = data.dropna() # for dropping the rows with the null values
    return data