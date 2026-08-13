import os
import pandas as pd
import pytest
from src.preprocess import load_and_clean_data, preprocess_data

def test_load_and_clean_data():
    data_path = 'data/raw/telecom_churn.csv'
    assert os.path.exists(data_path), "Dataset file should exist"
    
    df = load_and_clean_data(data_path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'total_charges' in df.columns
    assert df['total_charges'].isnull().sum() == 0

def test_preprocess_data_shapes():
    data_path = 'data/raw/telecom_churn.csv'
    df = load_and_clean_data(data_path)
    
    X_train, X_test, y_train, y_test, scaler, label_encoders = preprocess_data(df)
    
    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(X_train) + len(X_test) == len(df)
    assert len(y_train) == len(X_train)
    assert len(y_test) == len(X_test)
