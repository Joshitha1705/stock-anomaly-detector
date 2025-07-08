# anomaly_analyzer.py
# Custom module to detect anomalies in stock prices

import pandas as pd

def find_anomalies(data, threshold=0.05):
    """Detect anomalies based on percentage deviation from moving average.
    Args:
        data (pandas.DataFrame): Preprocessed stock data with Close and Moving_Avg.
        threshold (float): Percentage deviation to flag as anomaly (e.g., 0.04 = 4%).
    Returns:
        pandas.DataFrame: DataFrame with anomalies (Close, Deviation)."""
    if data is None or data.empty:
        return pd.DataFrame(columns=["Close", "Deviation"])
    
    data["Deviation"] = abs(data["Close"] - data["Moving_Avg"]) / data["Moving_Avg"]  # calculation of the devaiation

    anomalies = data[data["Deviation"] > threshold][["Close", "Deviation"]] # checking whether the deviation is exceded or not
    return anomalies