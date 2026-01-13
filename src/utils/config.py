"""
Global configuration file for CryptoPricePredict.
Modify these parameters to customize your analysis.
"""

import os

# =============================================================================
# 1. ASSET CONFIGURATION
# =============================================================================
# Change SYMBOL to any crypto ticker (e.g., "ETH", "BNB", "BTC")
SYMBOL = "BNB" 
MARKET = "USD"

# =============================================================================
# 2. FORECAST & BACKTEST CONFIGURATION
# =============================================================================
# How many months to predict into the future
FORECAST_MONTHS = 24 

# How many recent months to use for testing the model's accuracy
TEST_SIZE_MONTHS = 3

# How many months of history to show in the final chart
VISUALIZATION_HISTORY_MONTHS = 60 

# =============================================================================
# 3. MODEL SELECTION
# =============================================================================
# Available models: "RandomForest", "LinearRegression", "XGBoost" (if installed)
# Note: "RandomForest" is recommended for its robustness.
MODEL_TYPE = "LinearRegression" 

# Seed for reproducibility
RANDOM_STATE = 42

# =============================================================================
# 4. FEATURE ENGINEERING (Technical Indicators)
# =============================================================================
MA_WINDOWS = [3, 6]  # Moving Average windows
RSI_WINDOW = 6       # Relative Strength Index period
BB_WINDOW = 10       # Bollinger Bands period

# =============================================================================
# 5. FILE PATHS
# =============================================================================
RAW_DATA_PATH = f"data/raw/{SYMBOL.lower()}_monthly.csv"
PROCESSED_DATA_PATH = f"data/processed/{SYMBOL.lower()}_monthly.csv"
