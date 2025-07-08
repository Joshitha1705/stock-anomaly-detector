# anomaly_analyzer.py
# Module to detect unusual stock price movements for Techsophy project

import pandas as pd

def find_anomalies(data, threshold=0.02):  # Changed to 2%
    """
    Identify anomalies based on percentage deviation from moving average.
    Args:
        data (pandas.DataFrame): Preprocessed data with Close and Moving_Avg.
        threshold (float): Deviation threshold (e.g., 0.02 = 2%).
    Returns:
        pandas.DataFrame: Anomalies with Close and Deviation columns.
    """
    if data is None or data.empty:
        return pd.DataFrame(columns=["Close", "Deviation"])
    # Calculate percentage deviation from moving average
    data["Deviation"] = abs(data["Close"] - data["Moving_Avg"]) / data["Moving_Avg"]
    # Flag anomalies where deviation exceeds threshold
    anomalies = data[data["Deviation"] > threshold][["Close", "Deviation"]]
    return anomalies