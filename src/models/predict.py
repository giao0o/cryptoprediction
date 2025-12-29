"""
Generate future predictions.
"""

import pandas as pd


def predict_next_period(model, latest_features: pd.DataFrame):
    """
    Predict next period price.
    """
    prediction = model.predict(latest_features)
    return prediction[0]
