# 📊 CryptoPricePredict: Customization & Research Guide

This framework is designed for high flexibility, allowing you to easily swap assets, adjust forecasting horizons, and experiment with different machine learning models.

![image](https://github.com/giao0o/cryptoprediction/blob/main/tree.png) 

---

## 🛠 How to Customize Your Analysis

All primary customizations are handled within `src/utils/config.py`. You do **not** need to modify the core logic in most cases.

### 1. Change the Cryptocurrency
To predict a different coin (e.g., Ethereum), change the `SYMBOL` parameter:
```python
# src/utils/config.py
SYMBOL = "ETH"  # Options: "BTC", "ETH", "SOL", "ADA", etc.
```

### 2. Adjust the Forecast Duration
To change how many months into the future you want to predict:
```python
# src/utils/config.py
FORECAST_MONTHS = 12  # Predict 1 year ahead
```

### 3. Switch the Prediction Model
You can experiment with different algorithms by changing `MODEL_TYPE`:
```python
# src/utils/config.py
MODEL_TYPE = "LinearRegression"  # Options: "RandomForest", "LinearRegression"
```
*   **RandomForest**: Best for capturing complex, non-linear market patterns.
*   **LinearRegression**: Best for identifying simple long-term trends.

### 4. Adjust Visualization History
To see more or less historical context in your final chart:
```python
# src/utils/config.py
VISUALIZATION_HISTORY_MONTHS = 120  # Show 10 years of history
```

---

## 📂 Project Structure for Your Paper

When writing your seminar paper, you can refer to these modules:

| Module | Purpose in Research |
| :--- | :--- |
| `src/data/` | **Data Collection**: Methodology for sourcing financial time-series. |
| `src/features/` | **Feature Engineering**: Quantitative analysis using technical indicators. |
| `src/models/` | **Algorithm Selection**: Comparison of different ML architectures. |
| `src/evaluation/` | **Performance Metrics**: Statistical validation of model accuracy. |

---

## 🚀 Running the Program

1.  **Activate Environment**: `conda activate crypto-ml`
2.  **Execute**: `python3 src/main.py`
3.  **Output**: 
    *   `final_forecast_results.png`: The comprehensive visualization.
    *   Terminal output: Detailed metrics (RMSE, MAPE, etc.).

---

## 📌 Technical Support for MacBook
*   **M1/M2/M3 Chips**: The code is fully compatible. If you encounter a `ModuleNotFoundError`, ensure you are running the script from the root directory.
*   **Automatic Pathing**: The script automatically detects its location, so you can run it simply with `python3 src/main.py`.
