import pandas as pd

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Replacing specific values
data['Address'] = data['Address'].replace('Old Address', 'New Address')

# Example: Replace values in 'Price' column where price < 100000 with 'Low Price'
data['Price'] = data['Price'].apply(lambda x: 'Low Price' if x < 100000 else x)

print("\n=== Data After Value Replacement ===")
print(data.head())
