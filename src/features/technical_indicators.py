"""
Technical indicator calculations.
"""

import pandas as pd
import numpy as np

def moving_average(series: pd.Series, window: int) -> pd.Series:
    """Calculate moving average."""
    return series.rolling(window=window).mean()

def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    """Calculate Relative Strength Index (RSI)."""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    # Avoid division by zero
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def bollinger_bands(series: pd.Series, window: int = 20):
    """Calculate Bollinger Bands."""
    ma = series.rolling(window).mean()
    std = series.rolling(window).std()

    upper = ma + 2 * std
    lower = ma - 2 * std

    return ma, upper, lower
