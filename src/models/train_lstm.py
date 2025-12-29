"""
Train LSTM model for time series prediction.
"""

import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from src.utils.config import PROCESSED_DATA_PATH


def create_sequences(data, window_size=12):
    """Create rolling window sequences."""
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)


def train_lstm(window_size=12, epochs=50):
    df = pd.read_csv(PROCESSED_DATA_PATH, index_col=0, parse_dates=True)

    prices = df["close"].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    prices_scaled = scaler.fit_transform(prices)

    X, y = create_sequences(prices_scaled, window_size)

    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = Sequential([
        LSTM(64, return_sequences=False, input_shape=(window_size, 1)),
        Dense(1)
    ])

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    early_stop = EarlyStopping(
        patience=5,
        restore_best_weights=True
    )

    model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=16,
        callbacks=[early_stop],
        verbose=1
    )

    return model, scaler
