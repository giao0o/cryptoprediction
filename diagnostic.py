import pandas as pd
import numpy as np
import os

RAW_DATA_PATH = "/home/ubuntu/cryptoprediction/data/raw/btc_monthly.csv"

def load_raw_data():
    df = pd.read_csv(RAW_DATA_PATH, skiprows=3, header=None)
    df.columns = ["date", "close", "high", "low", "open", "volume"]
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    df = df.sort_index()
    df["close"] = pd.to_numeric(df["close"], errors='coerce')
    df["volume"] = pd.to_numeric(df["volume"], errors='coerce')
    return df.dropna(subset=["close", "volume"])

df = load_raw_data()
print(f"Loaded rows: {len(df)}")
print(df.head())

# Technical indicators
def moving_average(series, window):
    return series.rolling(window=window).mean()

def rsi(series, window=6):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def bollinger_bands(series, window=10):
    ma = series.rolling(window).mean()
    std = series.rolling(window).std()
    return ma, ma + 2 * std, ma - 2 * std

df["ma_3"] = moving_average(df["close"], 3)
df["ma_6"] = moving_average(df["close"], 6)
df["rsi"] = rsi(df["close"], 6)
ma, upper, lower = bollinger_bands(df["close"], 10)
df["bb_ma"] = ma
df["bb_upper"] = upper
df["bb_lower"] = lower

print(f"Rows after indicators: {len(df)}")
df_clean = df.dropna()
print(f"Rows after dropna: {len(df_clean)}")
print(df_clean.head())
