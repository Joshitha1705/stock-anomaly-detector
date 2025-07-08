
from stock_fetcher import get_stock_prices
from Data_cleaning import clean_stock_data
from Anomaly_analyzer import find_anomalies
from notifications import generate_alert

def run_anomaly_detector():
    """Main function to monitor stocks and detect anomalies."""

    stocks = ["AAPL", "MSFT", "GOOGL"]
    
    for stock in stocks:
        print(f"\n[Info] Analyzing {stock}...")

        raw_data = get_stock_prices(stock, time_frame="1d", frequency="1m")

        cleaned_data = clean_stock_data(raw_data)

        if cleaned_data is None:

            print(f"[Error] Skipping {stock} due to data issues")
            continue

        anomalies = find_anomalies(cleaned_data, threshold=0.05)  # 5% deviation
        generate_alert(stock, anomalies)

if __name__ == "__main__":
    run_anomaly_detector()