"""
Visualization utilities.
"""

import matplotlib.pyplot as plt


def plot_actual_vs_predicted(dates, actual, predicted):
    """Plot actual vs predicted prices."""
    plt.figure(figsize=(10, 5))
    plt.plot(dates, actual, label="Actual Price")
    plt.plot(dates, predicted, label="Predicted Price", marker="o")
    plt.legend()
    plt.title("Actual vs Predicted Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.savefig("backtest_results.png")
    print("Plot saved to backtest_results.png")
