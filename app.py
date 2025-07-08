from flask import Flask, render_template, request
from stock_fetcher import get_stock_prices
from Data_cleaning import clean_stock_data
from Anomaly_analyzer import find_anomalies
from notifications import generate_alert
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Store results for display
results = []

def process_stock(ticker):
    """
    Process a single stock for anomaly detection.
    Args:
        ticker (str): Stock symbol (e.g., 'TSLA').
    Returns:
        dict: Result with stock, status, and anomaly details.
    """
    ticker = ticker.upper().strip()
    raw_data = get_stock_prices(ticker, time_frame="5d", frequency="1m")
    if raw_data is None or raw_data.empty:
        return {"stock": ticker, "status": "error", "message": "No data available"}
    cleaned_data = clean_stock_data(raw_data)
    if cleaned_data is None:
        return {"stock": ticker, "status": "error", "message": "No data available"}
    anomalies = find_anomalies(cleaned_data, threshold=0.02)  # 2% threshold
    generate_alert(ticker, anomalies)  # Save to CSV
    if anomalies.empty:
        return {"stock": ticker, "status": "no_anomalies", "message": "No anomalies found"}
    anomalies_list = [
        {
            "time": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "price": f"${row['Close']:.2f}",
            "deviation": f"{row['Deviation']*100:.2f}%"
        }
        for timestamp, row in anomalies.iterrows()
    ]
    return {"stock": ticker, "status": "anomalies", "anomalies": anomalies_list}

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render the dashboard and handle stock ticker input.
    """
    global results
    if request.method == "POST":
        ticker = request.form.get("ticker")
        if ticker:
            result = process_stock(ticker)
            # Keep only the latest result
            results = [result]
        else:
            results = [{"stock": None, "status": "error", "message": "Please enter a valid stock ticker"}]
    return render_template("index.html", results=results, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    app.run(debug=True)