import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset
data = pd.read_csv('constituents.csv')

# Handling Missing Values
# Check for missing values
print("\n=== Missing Values ===")
print(data.isnull().sum())

# Drop columns with more than 15% missing values
threshold = 0.15 * len(data)
data_cleaned = data.loc[:, data.isnull().sum() < threshold]

# Separate numeric columns
numeric_cols = data_cleaned.select_dtypes(include=['number']).columns

# Fill missing values for numeric columns with mean
data_cleaned[numeric_cols] = data_cleaned[numeric_cols].fillna(data_cleaned[numeric_cols].mean())

# ============================
# Outliers Detection using Z-Score
# ============================

# Choose the column 'CIK' to detect outliers
if 'CIK' in data_cleaned.columns:
    # Compute z-scores for 'CIK'
    data_cleaned['z_score_cik'] = zscore(data_cleaned['CIK'])

    # Filter rows with z-scores above 3 or below -3
    outliers = data_cleaned[np.abs(data_cleaned['z_score_cik']) > 3]
    print("\n=== Outliers ===")
    print(outliers)

    # Visualizing the outliers in the 'CIK' column
    plt.figure(figsize=(10, 6))
    sns.boxplot(data_cleaned['CIK'])
    plt.title('Boxplot of CIK with Outliers')
    plt.show()

    # Remove outliers and display the dataset
    data_no_outliers = data_cleaned[np.abs(data_cleaned['z_score_cik']) <= 3]
    print("\n=== Data Without Outliers (Preview) ===")
    print(data_no_outliers.head())
else:
    print("The dataset does not contain the required column 'CIK'.")
