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

# Replacing specific values
data_cleaned_dedup['Address'] = data_cleaned_dedup['Address'].replace('Old Address', 'New Address')

# Example: Replace values in 'Price' column where price < 100000 with 'Low Price'
data_cleaned_dedup['Price'] = data_cleaned_dedup['Price'].apply(lambda x: 'Low Price' if x < 100000 else x)

print("\n=== Data After Value Replacement ===")
print(data_cleaned_dedup.head())
