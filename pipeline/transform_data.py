"""
transform_data.py

This script performs feature engineering on the cleaned dataset,
creating new variables that improve the predictive power of churn models.

It reads from the processed output of ingest_data.py, transforms the data,
and saves it for model training.
"""

# 1. Import necessary libraries
# (e.g., pandas, numpy, os, logging)

# 2. Define file paths
# Read from '../data/processed/cleaned_data.csv'
# Save output to '../data/processed/engineered_data.csv'

# 3. Load cleaned data
# Read the previously cleaned dataset into a DataFrame

# 4. Create new features
# Examples:
# - tenure_bins: categorize customers into tenure groups (e.g., 0-12, 13-24 months)
# - avg_monthly_spend = TotalCharges / tenure
# - interaction_term = MonthlyCharges * tenure
# - flag variables for services used (e.g., has_streaming, has_multiple_lines)

# 5. Encode categorical variables
# Use label encoding or one-hot encoding for columns like 'Contract', 'InternetService'
# Drop or keep original columns as needed

# 6. Normalize or scale features (optional)
# Apply MinMaxScaler, StandardScaler, or leave raw (depending on model choice)

# 7. Drop irrelevant or redundant columns
# Remove customer ID, or any features that leak target information

# 8. Save engineered dataset
# Export to '../data/processed/engineered_data.csv'

# 9. Log completion
# Print or log transformation summary (e.g., number of features created)
