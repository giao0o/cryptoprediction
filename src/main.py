"""
Main pipeline entry point.

Pipeline:
1. Fetch raw data
2. Preprocess data
3. Train ML model
4. Evaluate and visualize results
"""

from src.data.fetch_data import fetch_monthly_crypto_data
from src.data.preprocess import preprocess
from src.models.train_ml import train_random_forest
from src.visualization.plot_results import plot_actual_vs_predicted


def main():
    print("Step 1: Fetching raw data...")
    fetch_monthly_crypto_data()

    print("Step 2: Preprocessing data...")
    preprocess()

    print("Step 3: Training model...")
    model, X_test, y_test, preds = train_random_forest()

    print("Step 4: Visualizing results...")
    plot_actual_vs_predicted(
        dates=y_test.index,
        actual=y_test.values,
        predicted=preds
    )


if __name__ == "__main__":
    main()
