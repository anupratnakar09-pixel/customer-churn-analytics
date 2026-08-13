import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Load dataset and handle missing values."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}")

    df = pd.read_csv(file_path)

    # Convert total_charges to numeric, coercing errors to NaN
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

    # Fill missing values with median
    df['total_charges'] = df['total_charges'].fillna(
        df['total_charges'].median()
    )

    return df


def preprocess_data(
    df: pd.DataFrame, target_col: str = 'churn', test_size: float = 0.2
):
    """Encode categorical variables, scale numerical features, and split dataset."""
    df = df.copy()

    # Drop customer ID if present
    if 'customer_id' in df.columns:
        df = df.drop(columns=['customer_id'])

    # Encode binary target variable
    if target_col in df.columns:
        df[target_col] = df[target_col].map({'Yes': 1, 'No': 0})

    # Identify numerical and categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = df.select_dtypes(
        include=['int64', 'float64']
    ).columns.tolist()
    if target_col in numerical_cols:
        numerical_cols.remove(target_col)

    # Label encoding for categorical variables
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Split features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    # Standard Scale numerical features
    scaler = StandardScaler()
    X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
    X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

    return X_train, X_test, y_train, y_test, scaler, label_encoders


if __name__ == '__main__':
    data_path = 'data/raw/telecom_churn.csv'
    df = load_and_clean_data(data_path)
    X_train, X_test, y_train, y_test, scaler, encoders = preprocess_data(df)
    print(
        f'Data preprocessed successfully. Training set: {X_train.shape}, Test set: {X_test.shape}'
    )
