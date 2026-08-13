import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.tree import DecisionTreeClassifier

from preprocess import load_and_clean_data, preprocess_data


def train_and_evaluate(data_path: str, model_type: str = 'logistic'):
    """Train and evaluate the specified machine learning model."""
    df = load_and_clean_data(data_path)
    X_train, X_test, y_train, y_test, scaler, label_encoders = preprocess_data(
        df
    )

    if model_type == 'logistic':
        model = LogisticRegression(random_state=42, max_iter=1000)
    elif model_type == 'decision_tree':
        model = DecisionTreeClassifier(
            random_state=42, max_depth=5, criterion='entropy'
        )
    else:
        raise ValueError(f'Unsupported model type: {model_type}')

    # Fit Model
    model.fit(X_train, y_train)

    # Make Predictions
    y_pred = model.predict(X_test)
    y_proba = (
        model.predict_proba(X_test)[:, 1]
        if hasattr(model, 'predict_proba')
        else None
    )

    # Calculate Performance Metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, zero_division=0),
        'recall': recall_score(y_test, y_pred, zero_division=0),
        'f1': f1_score(y_test, y_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_test, y_proba)
        if y_proba is not None
        else 0.0,
    }

    print(f'=== {model_type.upper().replace("_", " ")} MODEL RESULTS ===')
    for metric, val in metrics.items():
        print(f'{metric.capitalize():<12}: {val:.4f}')
    print('\nClassification Report:\n', classification_report(y_test, y_pred))

    return model, metrics, X_train.columns


def get_feature_importance(model, feature_names):
    """Extract feature importance or coefficients from trained model."""
    if hasattr(model, 'coef_'):
        importance = model.coef_[0]
    elif hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
    else:
        return None

    df_importance = (
        pd.DataFrame({'Feature': feature_names, 'Importance': importance})
        .sort_values(by='Importance', ascending=False)
        .reset_index(drop=True)
    )

    return df_importance


if __name__ == '__main__':
    data_path = 'data/raw/telecom_churn.csv'

    print('--- Training Logistic Regression ---')
    lr_model, lr_metrics, feature_names = train_and_evaluate(
        data_path, model_type='logistic'
    )

    print('--- Training Decision Tree ---')
    dt_model, dt_metrics, _ = train_and_evaluate(
        data_path, model_type='decision_tree'
    )

    # Feature Importance for Decision Tree
    importance_df = get_feature_importance(dt_model, feature_names)
    print('--- Top Drivers of Churn (Decision Tree) ---')
    print(importance_df)
