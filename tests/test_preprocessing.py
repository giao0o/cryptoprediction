import pandas as pd
from src.data.preprocess import add_features


def test_feature_generation():
    dates = pd.date_range("2020-01-01", periods=30, freq="M")
    df = pd.DataFrame({
        "close": range(30),
        "volume": range(30)
    }, index=dates)

    df_feat = add_features(df)

    assert "rsi" in df_feat.columns
    assert "ma_3" in df_feat.columns
    assert "bb_upper" in df_feat.columns
    assert not df_feat.isnull().all().any()
