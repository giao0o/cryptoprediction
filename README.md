# 📊 CryptoPricePredict: Advanced Forecasting Framework

This project is a comprehensive Machine Learning pipeline designed for cryptocurrency price analysis, backtesting, and future forecasting. It is optimized for academic use in seminar papers and research projects.

---

## 🚀 Quick Start for macOS

1. **Setup Environment**:
   ```bash
   conda create -n crypto-ml python=3.11 -y
   conda activate crypto-ml
   pip install yfinance pandas scikit-learn matplotlib pyyaml requests
   ```

2. **Run the Pipeline**:
   ```bash
   python3 src/main.py
   ```

---

## ⚙️ Adjustable Parameters

You can customize the behavior of the model and visualization by editing `src/utils/config.py`.

### 1. Data & Asset Configuration
*   `SYMBOL`: The cryptocurrency ticker (default: `"BTC"`).
*   `MARKET`: The base currency (default: `"USD"`).
*   `RAW_DATA_PATH`: Location of the downloaded raw data.

### 2. Model & Forecast Configuration
*   `TEST_SIZE_MONTHS`: Number of recent months used for backtesting (default: `3`).
*   `FORECAST_MONTHS`: Number of months to predict into the future (default: `24`).
*   `RANDOM_STATE`: Seed for reproducibility (default: `42`).

### 3. Visualization Configuration
*   `VISUALIZATION_HISTORY_MONTHS`: Number of historical months to show in the final plot (default: `60`).

### 4. Technical Indicators (Feature Engineering)
*   `MA_WINDOWS`: List of windows for Moving Averages (e.g., `[3, 6]`).
*   `RSI_WINDOW`: Period for Relative Strength Index (default: `6`).
*   `BB_WINDOW`: Period for Bollinger Bands (default: `10`).

---

## 📂 Project Modules

*   **`src/data/fetch_data.py`**: Handles automated data retrieval from Yahoo Finance.
*   **`src/data/preprocess.py`**: Cleans data and generates technical features.
*   **`src/models/train_ml.py`**: Trains the Random Forest model and performs backtesting.
*   **`src/models/predict.py`**: Contains logic for multi-step future price projection.
*   **`src/visualization/plot_results.py`**: Generates the comprehensive analysis chart.

---

## 📈 Understanding the Output

After running the script, a file named `final_forecast_results.png` will be generated. It contains:
1.  **Historical Price (Gray)**: The long-term trend (adjustable via `VISUALIZATION_HISTORY_MONTHS`).
2.  **Actual Price (Blue)**: The real prices during the backtest period.
3.  **Predicted Price (Orange)**: The model's performance on known data.
4.  **Future Forecast (Green)**: Projected prices for the next 24 months (adjustable via `FORECAST_MONTHS`).
5.  **Confidence Interval**: Estimated range of future price movement.

---

## 🛠 Technical Notes for MacBook Users
*   **Path Issues**: The code now includes automatic path detection. You can run it from the root directory using `python3 src/main.py` without setting `PYTHONPATH`.
*   **Dependencies**: If you are on an M1/M2/M3 Mac, ensure your terminal is running under the correct architecture (ARM64) for optimal performance with `scikit-learn`.
