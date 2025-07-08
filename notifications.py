# notifications.py
import pandas as pd

def generate_alert(ticker, anomalies):
    """Save detected anomalies to CSV.
    Args:
        ticker (str): Stock symbol.
        anomalies (pandas.DataFrame): DataFrame with anomalies."""
    if not anomalies.empty:
        anomalies.to_csv(f"{ticker}_anomalies.csv", index_label="Time")