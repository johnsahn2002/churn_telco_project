"""
download_raw_data.py

Downloads the Telco Customer Churn dataset from Kaggle using the Kaggle API,
unzips it, and moves the dataset to the raw data folder as churn_data.csv.
"""

import os
import zipfile
import logging
import subprocess

# Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
dataset = 'blastchar/telco-customer-churn'
raw_dir = '../data/raw/'
output_zip = 'telco-customer-churn.zip'
target_file = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
final_name = 'churn_data.csv'

def download_dataset():
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)
        logging.info(f"Created directory: {raw_dir}")

    logging.info("Downloading dataset from Kaggle...")
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset], check=True)

    logging.info("Unzipping dataset...")
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(raw_dir)

    logging.info("Renaming file...")
    os.rename(os.path.join(raw_dir, target_file), os.path.join(raw_dir, final_name))

    logging.info("Cleaning up...")
    os.remove(output_zip)

    logging.info(f"Dataset ready at {raw_dir}{final_name}")

if __name__ == "__main__":
    download_dataset()
