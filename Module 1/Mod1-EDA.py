import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('constituents.csv')

# Check missing values
print("\n=== Missing Values ===")
print(data.isnull().sum())

# Drop columns with more than 15% missing values
threshold = 0.15 * len(data)
data_cleaned = data.loc[:, data.isnull().sum() < threshold]

# Separate numeric and non-numeric columns
numeric_cols = data_cleaned.select_dtypes(include=['number']).columns
non_numeric_cols = data_cleaned.select_dtypes(exclude=['number']).columns

# Fill missing values for numeric columns with the mean
data_cleaned[numeric_cols] = data_cleaned[numeric_cols].fillna(data_cleaned[numeric_cols].mean())

print("\n=== Cleaned Data (Preview) ===")
print(data_cleaned.head())

# ==========================
# Visualization Techniques
# ==========================

# Plot histogram for 'CIK' column (a numeric column)
if 'CIK' in numeric_cols:
    sns.histplot(data_cleaned['CIK'], kde=True)
    plt.title('Histogram of CIK')
    plt.xlabel('CIK')
    plt.ylabel('Frequency')
    plt.show()

# Scatter plot for 'CIK' vs 'Founded' (both numeric columns)
if 'CIK' in numeric_cols and 'Founded' in numeric_cols:
    plt.scatter(data_cleaned['CIK'], data_cleaned['Founded'])
    plt.title('CIK vs Founded')
    plt.xlabel('CIK')
    plt.ylabel('Founded')
    plt.show()
