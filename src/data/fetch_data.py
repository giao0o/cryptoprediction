"""
Fetch cryptocurrency data from Alpha Vantage API
and save raw JSON data locally.
"""

import json
import requests
from src.utils.config import (
    ALPHA_VANTAGE_API_KEY,
    SYMBOL,
    MARKET,
    RAW_DATA_PATH
)


def fetch_monthly_crypto_data():
    """
    Fetch monthly cryptocurrency price data from Alpha Vantage.
    """
    url = (
        "https://www.alphavantage.co/query"
        f"?function=DIGITAL_CURRENCY_MONTHLY"
        f"&symbol={SYMBOL}"
        f"&market={MARKET}"
        f"&apikey={ALPHA_VANTAGE_API_KEY}"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    # Save raw JSON
    with open(RAW_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("Raw data saved to:", RAW_DATA_PATH)


if __name__ == "__main__":
    fetch_monthly_crypto_data()
