"""
Fetch cryptocurrency data from Yahoo Finance API
and save raw CSV data locally.
"""

import yfinance as yf
import pandas as pd
import os
from src.utils.config import (
    SYMBOL,
    MARKET,
    RAW_DATA_PATH
)

def fetch_monthly_crypto_data():
    """
    Fetch monthly cryptocurrency price data from Yahoo Finance.
    """
    ticker_symbol = f"{SYMBOL}-{MARKET}"
    print(f"Fetching data for {ticker_symbol}...")
    
    # Fetch historical data
    # period="max" to get all available data
    # interval="1mo" for monthly data
    data = yf.download(ticker_symbol, period="max", interval="1mo")
    
    if data.empty:
        print("No data found.")
        return

    # Ensure directory exists
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    
    # Save to CSV (yfinance returns a DataFrame)
    # We'll change the RAW_DATA_PATH to .csv in config or handle it here
    csv_path = RAW_DATA_PATH.replace(".json", ".csv")
    data.to_csv(csv_path)
    
    print("Raw data saved to:", csv_path)

if __name__ == "__main__":
    fetch_monthly_crypto_data()
