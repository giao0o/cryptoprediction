"""
Global configuration file.
Store API keys, file paths, and global parameters here.
"""

import os

# ======================
# API CONFIGURATION
# ======================
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "YOUR_API_KEY")

# ======================
# DATA CONFIGURATION
# ======================
SYMBOL = "BTC"
MARKET = "USD"

RAW_DATA_PATH = "data/raw/btc_monthly.json"
PROCESSED_DATA_PATH = "data/processed/btc_monthly.csv"

# ======================
# MODEL CONFIGURATION
# ======================
RANDOM_STATE = 42
TEST_SIZE_MONTHS = 3

# ======================
# FEATURE CONFIGURATION
# ======================
MA_WINDOWS = [3, 6, 12]
RSI_WINDOW = 14
BB_WINDOW = 20
