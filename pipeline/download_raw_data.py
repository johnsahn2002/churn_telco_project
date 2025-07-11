"""
download_raw_data.py

Downloads the Telco Customer Churn dataset from Kaggle using the Kaggle API,
unzips it, and moves the dataset to the raw data folder as churn_data.csv.
"""

import os
import zipfile
import kaggle

def download_dataset(dataset_name: str, download_path: str):
    os.makedirs(download_path, exist_ok=True)
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"✅ Downloaded and extracted: {dataset_name}")

if __name__ == "__main__":
    dataset = "blastchar/telco-customer-churn"
    output_dir = "data/raw"
    download_dataset(dataset, output_dir)
