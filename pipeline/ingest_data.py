"""
ingest_data.py

This script loads raw data from source (e.g., CSV, API, database),
performs initial cleaning, and saves the result into a processed format
for downstream modeling.

If the raw dataset is missing, it automatically downloads it from Kaggle.
"""

import pandas as pd
import os
import logging
from datetime import datetime
import sys
import numpy as np
import warnings
import subprocess

warnings.filterwarnings("ignore")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ingest_data.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def log_script_start_end(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Starting {func.__name__} at {datetime.now()}")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__} at {datetime.now()}")
        return result
    return wrapper

@log_script_start_end
def main():
    raw_data_path = '../data/raw/churn_data.csv'
    processed_data_path = '../data/processed/cleaned_data.csv'

    # Create directories
    os.makedirs('../data/raw/', exist_ok=True)
    os.makedirs('../data/processed/', exist_ok=True)

    # Auto-download if raw file is missing
    if not os.path.isfile(raw_data_path):
        logging.warning(f"Raw data file not found: {raw_data_path}")
        logging.info("Attempting to download dataset from Kaggle...")
        try:
            subprocess.run(['python', 'pipeline/download_raw_data.py'], check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Download script failed: {e}")
            sys.exit(1)

    # Load raw data
    try:
        df = pd.read_csv(raw_data_path)
        logging.info(f"Loaded raw data with shape: {df.shape}")
    except Exception as e:
        logging.error(f"Error loading raw data: {e}")
        sys.exit(1)

    if df.empty:
        logging.error("Loaded DataFrame is empty.")
        sys.exit(1)

    # Basic inspection
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.dropna(subset=['churn'], inplace=True)
    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
    df['totalcharges'].fillna(0, inplace=True)
    df.dropna(subset=['totalcharges', 'monthlycharges', 'customerid'], inplace=True)
    df.dropna(inplace=True)
    df['customerid'] = df['customerid'].astype(str)
    df['churn'] = df['churn'].astype('category')

    # Metadata
    metadata = pd.DataFrame({
        'column_name': df.columns,
        'data_type': df.dtypes.values,
        'missing_values': df.isnull().sum().values
    })
    metadata.to_csv('../data/processed/metadata.csv', index=False)
    logging.info("Saved metadata.")

    # Save cleaned data
    try:
        df.to_csv(processed_data_path, index=False)
        logging.info(f"Cleaned data saved to {processed_data_path}")
    except Exception as e:
        logging.error(f"Error saving cleaned data: {e}")
        sys.exit(1)

    return df

if __name__ == "__main__":
    main()
