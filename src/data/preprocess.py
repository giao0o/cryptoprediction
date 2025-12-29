"""
Data cleaning and feature engineering.
"""

import json
import pandas as pd
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
    """Load raw JSON data and convert to DataFrame."""
    with open(RAW_DATA_PATH, "r") as f:
        raw = json.load(f)

    df = pd.DataFrame(raw["Time Series (Digital Currency Monthly)"]).T
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    # Use USD closing price
    df["close"] = df["4a. close (USD)"].astype(float)
    df["volume"] = df["5. volume"].astype(float)

    return df[["close", "volume"]]


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add technical indicators and time features."""
    for w in MA_WINDOWS:
        df[f"ma_{w}"] = moving_average(df["close"], w)

    df["rsi"] = rsi(df["close"], RSI_WINDOW)

    bb_ma, bb_upper, bb_lower = bollinger_bands(df["close"], BB_WINDOW)
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
    df.to_csv(PROCESSED_DATA_PATH)

    print("Processed data saved to:", PROCESSED_DATA_PATH)


if __name__ == "__main__":
    preprocess()
