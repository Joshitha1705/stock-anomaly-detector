
import pandas as pd

def find_anomalies(data, threshold=0.05): 
    """
    Identify anomalies based on percentage deviation from moving average.
    Args:
        data (pandas.DataFrame): Preprocessed data with Close and Moving_Avg.
        threshold (float): Deviation threshold (e.g., 0.05 = 5%).
    Returns:
        pandas.DataFrame: Anomalies with Close and Deviation columns.
    """
    if data is None or data.empty:
        return pd.DataFrame(columns=["Close", "Deviation"])
    data["Deviation"] = abs(data["Close"] - data["Moving_Avg"]) / data["Moving_Avg"]
    
    anomalies = data[data["Deviation"] > threshold][["Close", "Deviation"]]
    return anomalies