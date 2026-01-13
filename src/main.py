"""
Main pipeline entry point.
"""

import os
import sys
import pandas as pd

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.data.fetch_data import fetch_monthly_crypto_data
from src.data.preprocess import preprocess
from src.models.train_ml import train_model
from src.models.predict import forecast_future
from src.visualization.plot_results import plot_comprehensive_results
from src.utils.config import PROCESSED_DATA_PATH

def main():
    print("Step 1: Fetching raw data...")
    fetch_monthly_crypto_data()

    print("Step 2: Preprocessing data...")
    preprocess()

    print("Step 3: Training model & Backtesting...")
    model, X_test, y_test, test_preds = train_model()
    
    # Load full processed data for visualization
    df_processed = pd.read_csv(PROCESSED_DATA_PATH, index_col=0, parse_dates=True)
    feature_cols = X_test.columns

    print("Step 4: Generating Future Forecast...")
    future_preds = forecast_future(model, df_processed, feature_cols)

    print("Step 5: Visualizing Comprehensive Results...")
    plot_comprehensive_results(
        historical_data=df_processed,
        test_actual=y_test,
        test_preds=test_preds,
        future_preds=future_preds
    )
    
    # Print metrics
    from src.evaluation.metrics import rmse, mape, directional_accuracy
    print("\n--- Backtest Performance Metrics ---")
    print(f"RMSE: {rmse(y_test.values, test_preds):.2f}")
    print(f"MAPE: {mape(y_test.values, test_preds):.2f}%")
    if len(y_test) > 1:
        print(f"Directional Accuracy: {directional_accuracy(y_test.values, test_preds):.2%}")
    print("------------------------------------\n")

if __name__ == "__main__":
    main()
