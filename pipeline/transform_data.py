"""
transform_data.py

This script performs feature engineering on the cleaned dataset,
creating new variables that improve the predictive power of churn models.

It reads from the processed output of ingest_data.py, transforms the data,
and saves it for model training.
"""

# pipeline/transform_data.py

import pandas as pd
import os

def transform_features(input_path, output_path):
    print("Loading cleaned data...")
    df = pd.read_csv(input_path)

    # Tenure groupings
    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, 72],
        labels=['0-12', '12-24', '24-48', '48-60', '60+']
    )

    # MonthlyCharges / Tenure ratio
    df['monthly_charge_ratio'] = df['monthlycharges'] / (df['tenure'] + 1)

    # Binary indicator: has tech support
    df['has_tech_support'] = df['techsupport'].map({'Yes': 1, 'No': 0})

    # Binary indicator: uses paperless billing
    df['paperless_billing'] = df['paperlessbilling'].map({'Yes': 1, 'No': 0})

    # Binary indicator: has streaming services
    df['has_streaming_services'] = df[['streamingtv', 'streamingmovies']].apply(
        lambda row: int('Yes' in row.values), axis=1
    )

    # Target column to binary
    df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})

    # Save transformed file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Transformed data saved to {output_path}")

if __name__ == "__main__":
    input_file = "data/processed/cleaned_telco.csv"
    output_file = "data/processed/transformed_telco.csv"
    transform_features(input_file, output_file)
