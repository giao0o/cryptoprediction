"""
Visualization utilities.
"""

import matplotlib.pyplot as plt
import pandas as pd
from src.utils.config import VISUALIZATION_HISTORY_MONTHS

def plot_comprehensive_results(historical_data, test_actual, test_preds, future_preds):
    """
    Plot historical trend, backtest results, and future forecast.
    """
    plt.figure(figsize=(14, 7))
    
    # 1. Plot Historical Data (last N months)
    history = historical_data.tail(VISUALIZATION_HISTORY_MONTHS)
    plt.plot(history.index, history['close'], label="Historical Price", color='gray', alpha=0.5)
    
    # 2. Plot Backtest Results (Actual vs Predicted)
    plt.plot(test_actual.index, test_actual.values, label="Actual Price (Test)", color='blue', linewidth=2)
    plt.plot(test_actual.index, test_preds, label="Predicted Price (Backtest)", color='orange', linestyle='--', marker='o')
    
    # 3. Plot Future Forecast
    plt.plot(future_preds.index, future_preds.values, label="Future Forecast (24m)", color='green', linestyle=':', linewidth=2)
    plt.fill_between(future_preds.index, future_preds.values * 0.8, future_preds.values * 1.2, color='green', alpha=0.1, label="Confidence Interval (Est.)")
    
    plt.title(f"Cryptocurrency Price Analysis: History, Backtest & Future Forecast", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    # Highlight the transition to future
    plt.axvline(x=test_actual.index[-1], color='red', linestyle='-', alpha=0.3)
    plt.text(test_actual.index[-1], plt.ylim()[0], ' Future Start', color='red', verticalalignment='bottom')

    plt.tight_layout()
    plt.savefig("final_forecast_results.png")
    print("Comprehensive plot saved to final_forecast_results.png")
