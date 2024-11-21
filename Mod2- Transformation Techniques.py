import pandas as pd

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Check for duplicates
print("\n=== Checking for Duplicates ===")
print(f"Number of duplicate rows: {data.duplicated().sum()}")

# Remove duplicate rows
data_cleaned_dedup = data.drop_duplicates()

print("\n=== Data After Deduplication ===")
print(data_cleaned_dedup.head())
