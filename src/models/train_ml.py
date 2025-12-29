"""
Train traditional machine learning models.
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from src.utils.config import (
    PROCESSED_DATA_PATH,
    RANDOM_STATE,
    TEST_SIZE_MONTHS
)


def train_random_forest():
    """Train Random Forest model for price prediction."""
    df = pd.read_csv(PROCESSED_DATA_PATH, index_col=0, parse_dates=True)

    X = df.drop(columns=["close"])
    y = df["close"]

    X_train = X[:-TEST_SIZE_MONTHS]
    X_test = X[-TEST_SIZE_MONTHS:]
    y_train = y[:-TEST_SIZE_MONTHS]
    y_test = y[-TEST_SIZE_MONTHS:]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=RANDOM_STATE
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    print(f"MAE: {mae:.2f}")

    return model, X_test, y_test, preds


if __name__ == "__main__":
    train_random_forest()
