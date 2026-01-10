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
    
    # --- Step 6: Export Results to Excel with Professional English Comments ---
    print("Step 6: Exporting Results to Excel...")

    # 1. Handle Future Forecast Data and Generate Future Dates
    # Ensure future_values is a 1D array even if input is a Series or higher-dim array
    future_values = future_preds.values.flatten() if isinstance(future_preds, pd.Series) else future_preds.flatten()
    
    # Identify the last timestamp from the processed historical data
    # Ensure the index is in datetime format to perform frequency-based arithmetic
    last_date = pd.to_datetime(df_processed.index[-1])
    
    # Generate a range of future dates starting from the month after last_date
    # 'ME' stands for Month End; use 'MS' if your data starts at the beginning of the month
    future_dates = pd.date_range(start=last_date, periods=len(future_values) + 1, freq='ME')[1:]

    # Create DataFrame for future predictions with explicit Date column
    export_future_results = pd.DataFrame({
        'Date': future_dates,
        'Future_Forecast': future_values
    })

    # 2. Prepare Backtest Results (Test Set Performance)
    # Align actual vs predicted values and calculate error residuals
    actuals = y_test.values.flatten() if hasattr(y_test, 'values') else y_test
    preds = test_preds.flatten()
    
    export_test_results = pd.DataFrame({
        'Actual_Value': actuals,
        'Predicted_Value': preds,
        'Residual': (actuals - preds),  # Error term for residual analysis in the paper
        'Abs_Percentage_Error': abs((actuals - preds) / actuals) # Used for MAPE calculation
    }, index=y_test.index)

    # 3. Export to Multi-Sheet Excel File
    # Define output path relative to the project root
    output_path = os.path.join(project_root, 'results', 'model_performance_report.xlsx')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with pd.ExcelWriter(output_path) as writer:
        # Sheet 1: Detailed backtesting data with residuals for error distribution analysis
        export_test_results.to_excel(writer, sheet_name='Backtest_Details')
        
        # Sheet 2: Future forecast values with corresponding timestamps
        export_future_results.to_excel(writer, sheet_name='Future_Forecast', index=False)
        
        # Sheet 3: Global performance summary for the 'Results' section of the paper
        from src.evaluation.metrics import rmse, mape, directional_accuracy
        metrics_summary = pd.DataFrame({
            'Metric': ['RMSE', 'MAPE', 'Directional Accuracy'],
            'Value': [
                f"{rmse(actuals, preds):.4f}",
                f"{mape(actuals, preds):.2f}%",
                f"{directional_accuracy(actuals, preds):.2%}"
            ]
        })
        metrics_summary.to_excel(writer, sheet_name='Global_Metrics', index=False)

    print(f"Academic report data with dates saved to: {output_path}")
    
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
