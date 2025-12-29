"""
Evaluation metrics for time series prediction.
"""

import numpy as np


def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))


def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def directional_accuracy(y_true, y_pred):
    """Measure prediction direction correctness."""
    return np.mean(
        (np.diff(y_true) * np.diff(y_pred)) > 0
    )
