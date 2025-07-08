
def generate_alert(ticker, anomalies):

    """Generate console alerts for detected anomalies.
    Args:
        ticker (str): Stock symbol.
        anomalies (pandas.DataFrame): DataFrame with anomalies."""
    if anomalies.empty:
        print(f"[Info] No anomalies found for {ticker}")
        return
    print(f"[ALERT] Anomalies detected for {ticker}:")

    for timestamp, row in anomalies.iterrows():

        print(f"Time: {timestamp}, Price: ${row['Close']:.2f}, "
              
              f"Deviation: {row['Deviation']*100:.2f}%")