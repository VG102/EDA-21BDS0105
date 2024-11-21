import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset
data = pd.read_csv('housing_data.csv')

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

# Choose the column 'Price' to detect outliers
if 'Price' in data_cleaned.columns:
    # Compute z-scores for 'Price'
    data_cleaned['z_score_price'] = zscore(data_cleaned['Price'])

    # Filter rows with z-scores above 3 or below -3
    outliers = data_cleaned[np.abs(data_cleaned['z_score_price']) > 3]
    print("\n=== Outliers ===")
    print(outliers)

    # Visualizing the outliers in the 'Price' column
    plt.figure(figsize=(10, 6))
    sns.boxplot(data_cleaned['Price'])
    plt.title('Boxplot of Price with Outliers')
    plt.show()

    # Remove outliers and display the dataset
    data_no_outliers = data_cleaned[np.abs(data_cleaned['z_score_price']) <= 3]
    print("\n=== Data Without Outliers (Preview) ===")
    print(data_no_outliers.head())
else:
    print("The dataset does not contain the required column 'Price'.")
