import pandas as pd

# Load the dataset
data = pd.read_csv('constituents.csv')

# Check for missing values
print("\n=== Missing Values ===")
print(data.isnull().sum())

# Drop columns with more than 15% missing values
threshold = 0.15 * len(data)
data_cleaned = data.loc[:, data.isnull().sum() < threshold]

# Separate numeric and non-numeric columns
numeric_cols = data_cleaned.select_dtypes(include=['number']).columns

# Fill missing values for numeric columns with mean
data_cleaned[numeric_cols] = data_cleaned[numeric_cols].fillna(data_cleaned[numeric_cols].mean())

# Display cleaned data
print("\n=== Cleaned Data (Preview) ===")
print(data_cleaned.head())
