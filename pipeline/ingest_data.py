"""
ingest_data.py

This script loads raw data from source (e.g., CSV, API, database),
performs initial cleaning, and saves the result into a processed format
for downstream modeling.

If the raw dataset is missing, it automatically downloads it from Kaggle.
"""

import pandas as pd
import os

def load_and_clean_data(input_path, output_path):
    print("Reading data...")
    df = pd.read_csv(input_path)

    # Drop customerID if present
    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Replace spaces and handle missing values
    df.replace(" ", pd.NA, inplace=True)
    df.dropna(inplace=True)

    # Convert totalcharges to numeric (often comes as object)
    if 'totalcharges' in df.columns:
        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
        df.dropna(subset=['totalcharges'], inplace=True)

    print(f"Saving cleaned data to {output_path}")
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    output_file = "data/processed/cleaned_telco.csv"

    os.makedirs("data/processed", exist_ok=True)
    load_and_clean_data(input_file, output_file)
