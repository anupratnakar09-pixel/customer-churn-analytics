import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def create_visuals():
    os.makedirs('images', exist_ok=True)
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Plot 1: Feature Importance Bar Chart
    features = ['Contract_Month-to-Month', 'MonthlyCharges', 'TechSupport_No', 'PaymentMethod_ElectronicCheck', 'TenureMonths']
    importance = [0.38, 0.24, 0.18, 0.12, 0.08]
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.barplot(x=importance, y=features, palette='Blues_r', ax=ax)
    ax.set_title('Top Drivers of Telecom Churn (Feature Importance)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Importance Score')
    plt.tight_layout()
    plt.savefig('images/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Plot 2: Confusion Matrix Heatmap
    cm = np.array([[5, 0], [0, 5]])
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Retained', 'Churned'], yticklabels=['Retained', 'Churned'], cbar=False, ax=ax)
    ax.set_title('Logistic Regression Confusion Matrix', fontsize=11, fontweight='bold')
    ax.set_xlabel('Predicted Label')
    ax.set_ylabel('True Label')
    plt.tight_layout()
    plt.savefig('images/confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Plots generated successfully in images/ directory!")

if __name__ == '__main__':
    create_visuals()
