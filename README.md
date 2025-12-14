# 📊 Crypto Prediction

Predict cryptocurrency prices using **Machine Learning** and **Python**.  
This project fetches data from [Alpha Vantage](https://www.alphavantage.co/documentation/#digital-currency) and predicts monthly and quarterly price trends.
## 🗂 Project Structure

The project is organized in a modular and scalable way to support data collection, preprocessing, modeling, evaluation, and visualization.

```text
crypto-prediction/
│
├── data/
│   ├── raw/                    # Raw data fetched from Alpha Vantage
│   │   └── btc_monthly.json
│   │
│   ├── processed/              # Cleaned and feature-engineered datasets
│   │   └── btc_monthly.csv
│
├── notebooks/                  # Jupyter notebooks for exploration & experiments
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_experiments.ipynb
│
├── src/
│   ├── data/
│   │   ├── fetch_data.py        # API calls to Alpha Vantage
│   │   └── preprocess.py       # Data cleaning & feature engineering
│   │
│   ├── features/
│   │   └── technical_indicators.py  # MA, RSI, Bollinger Bands, etc.
│   │
│   ├── models/
│   │   ├── train_ml.py          # Train traditional ML models
│   │   ├── train_lstm.py        # Train deep learning models (LSTM/GRU)
│   │   └── predict.py           # Generate predictions
│   │
│   ├── evaluation/
│   │   └── metrics.py           # MAE, RMSE, MAPE, directional accuracy
│   │
│   ├── visualization/
│   │   └── plot_results.py      # Price & prediction visualizations
│   │
│   └── utils/
│       ├── config.py            # Global configuration & parameters
│       └── helpers.py           # Utility functions
│
├── configs/
│   └── model_config.yaml        # Model hyperparameters
│
├── tests/
│   └── test_preprocessing.py    # Unit tests
│
├── .gitignore
├── requirements.txt             # Python dependencies
├── README.md
└── LICENSE
```

---

## 📚 Table of Contents

- [🔑 1. Get API Key & Explore Data](#-1-get-api-key--explore-data)
- [🧹 2. Data Cleaning & Preprocessing](#-2-data-cleaning--preprocessing)
- [🎯 3. Define Prediction Targets](#-3-define-prediction-targets)
- [⚙️ 4. Choose Models](#-4-choose-models)
- [🗂 5. Split Data](#-5-split-data)
- [🤖 6. Train & Predict](#-6-train--predict)
- [📈 7. Visualization](#-7-visualization)
- [💻 8. Version Control & GitHub](#-8-version-control--github)
- [🚀 9. Future Improvements](#-9-future-improvements)
- [📌 References](#-references)

---

## 🔑 1. Get API Key & Explore Data

1. Register at [Alpha Vantage](https://www.alphavantage.co/) to get your **API Key**.
2. Explore the Digital Currency API endpoints:  
   - `DIGITAL_CURRENCY_DAILY`  
   - `DIGITAL_CURRENCY_WEEKLY`  
   - `DIGITAL_CURRENCY_MONTHLY`  

3. Example: Fetch monthly BTC data

```python
import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"
symbol = "BTC"
market = "USD"

url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={symbol}&market={market}&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data['Time Series (Digital Currency Monthly)']).T
df = df.astype(float)
df.index = pd.to_datetime(df.index)
print(df.head())
```

## 🧹 2. Data Cleaning & Preprocessing

### Key Preprocessing Steps

- Sort data in chronological order  
- Handle missing values (`NaN`)  
- Convert prices and volume to numeric format  

### Feature Engineering

- 📈 Moving Averages (MA)  
- 📊 RSI  
- 📉 Bollinger Bands  
- 📅 Date features (month, quarter)  

### Feature Scaling

- Standardization or normalization for machine learning models  

---

## 🎯 3. Define Prediction Targets

### Monthly Prediction

Predict next month’s:
- Closing price  
- Return percentage  

### Quarterly Prediction

- Aggregate monthly data into quarters  
- Predict:
  - Quarterly closing price  
  - Quarterly return  

### Problem Types

- **Regression** → Predict actual price values  
- **Classification** → Predict direction (up / down)  

---

## ⚙️ 4. Choose Models

### Traditional Machine Learning

- Linear Regression  
- Random Forest Regressor  
- XGBoost  
- LightGBM  

### Deep Learning (Time Series)

- LSTM  
- GRU  
- Temporal Convolutional Networks (TCN)  

### Advanced Techniques

- Ensemble learning  
- Lagged price features  
- Technical indicators as model inputs  

---

## 🗂 5. Split Data

Time-series data is split **by time**, not randomly:

```python
train = df[:-3]   # all but last 3 months
test = df[-3:]    # last 3 months as test set
```

---

## 🤖 6. Train & Predict

### Example: Random Forest Regression

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print(f"MAE: {mae:.4f}")
```

---

## 📈 7. Visualization

Visualize actual vs predicted prices to compare model performance over time.  
This helps identify trends, prediction errors, and potential model bias.

---

## 💻 8. Version Control & GitHub

### Recommended Git Workflow

- `main` → stable, production-ready code  
- `feature_engineering` → feature experiments  
- `lstm_experiment` → deep learning models  

### Example Git Commands

- `git add .`  
- `git commit -m "Initial crypto prediction pipeline"`  
- `git push origin main`  

---

## 🚀 9. Future Improvements

- 📊 Add trading volume and on-chain metrics  
- 🧠 Integrate sentiment analysis from news or social media  
- 🔄 Multi-asset prediction (BTC, ETH, LTC)  
- ⏱ Multi-step forecasting (3–6 months ahead)  
- ⚡ Hyperparameter tuning and model ensembling  

---

## 📌 References

- Alpha Vantage Digital Currency API  
  https://www.alphavantage.co/documentation/#digital-currency  

- Scikit-learn  
  https://scikit-learn.org/stable/  

- Pandas  
  https://pandas.pydata.org/docs/  

- Matplotlib  
  https://matplotlib.org/stable/



