"""
Train machine learning models using a factory pattern.
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from src.utils.config import (
    PROCESSED_DATA_PATH,
    RANDOM_STATE,
    TEST_SIZE_MONTHS,
    MODEL_TYPE
)

def get_model():
    """Model Factory: Returns the model specified in config.py."""
    if MODEL_TYPE == "RandomForest":
        return RandomForestRegressor(n_estimators=200, random_state=RANDOM_STATE)
    elif MODEL_TYPE == "LinearRegression":
        return LinearRegression()
    else:
        print(f"Unknown model type: {MODEL_TYPE}. Defaulting to RandomForest.")
        return RandomForestRegressor(n_estimators=200, random_state=RANDOM_STATE)

def train_model():
    """Train the selected model and perform backtesting."""
    df = pd.read_csv(PROCESSED_DATA_PATH, index_col=0, parse_dates=True)

    X = df.drop(columns=["close"])
    y = df["close"]

    # Split data chronologically
    X_train = X[:-TEST_SIZE_MONTHS]
    X_test = X[-TEST_SIZE_MONTHS:]
    y_train = y[:-TEST_SIZE_MONTHS]
    y_test = y[-TEST_SIZE_MONTHS:]

    model = get_model()
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, preds)
    print(f"Model: {MODEL_TYPE} | Backtest MAE: {mae:.2f}")

    return model, X_test, y_test, preds

if __name__ == "__main__":
    train_model()
