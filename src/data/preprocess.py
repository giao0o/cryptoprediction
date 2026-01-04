"""
Data cleaning and feature engineering.
"""

import pandas as pd
import os
from src.features.technical_indicators import (
    moving_average,
    rsi,
    bollinger_bands
)
from src.utils.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    MA_WINDOWS,
    RSI_WINDOW,
    BB_WINDOW
)

def load_raw_data() -> pd.DataFrame:
    """Load raw CSV data and convert to DataFrame."""
    csv_path = RAW_DATA_PATH.replace(".json", ".csv")
    
    # Read the CSV
    # Row 0: Price, Close, High, Low, Open, Volume
    # Row 1: Ticker, BTC-USD, ...
    # Row 2: Date, (empty), ...
    # Row 3+: Data
    df = pd.read_csv(csv_path, skiprows=3, header=None)
    
    # Assign column names based on the structure we saw
    # Column 0 is Date, 1 is Close, 2 is High, 3 is Low, 4 is Open, 5 is Volume
    df.columns = ["date", "close", "high", "low", "open", "volume"]
    
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    df = df.sort_index()

    # Convert to numeric and drop any non-numeric rows
    df["close"] = pd.to_numeric(df["close"], errors='coerce')
    df["volume"] = pd.to_numeric(df["volume"], errors='coerce')
    
    df = df.dropna(subset=["close", "volume"])

    return df[["close", "volume"]]

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add technical indicators and time features."""
    # Ensure data is 1D for indicators
    close_series = df["close"]
    
    for w in MA_WINDOWS:
        df[f"ma_{w}"] = moving_average(close_series, w)

    df["rsi"] = rsi(close_series, RSI_WINDOW)

    bb_ma, bb_upper, bb_lower = bollinger_bands(close_series, BB_WINDOW)
    df["bb_ma"] = bb_ma
    df["bb_upper"] = bb_upper
    df["bb_lower"] = bb_lower

    # Date-based features
    df["month"] = df.index.month
    df["quarter"] = df.index.quarter

    return df

def preprocess():
    """Full preprocessing pipeline."""
    df = load_raw_data()
    df = add_features(df)

    df = df.dropna()
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH)

    print("Processed data saved to:", PROCESSED_DATA_PATH)

if __name__ == "__main__":
    preprocess()
