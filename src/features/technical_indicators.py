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
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    avg_gain = pd.Series(gain).rolling(window).mean()
    avg_loss = pd.Series(loss).rolling(window).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def bollinger_bands(series: pd.Series, window: int = 20):
    """Calculate Bollinger Bands."""
    ma = series.rolling(window).mean()
    std = series.rolling(window).std()

    upper = ma + 2 * std
    lower = ma - 2 * std

    return ma, upper, lower
