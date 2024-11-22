import pandas as pd

# Load the dataset
data = pd.read_csv('constituents.csv')

# Replacing specific values in 'Headquarters Location'
data['Headquarters Location'] = data['Headquarters Location'].replace('Old Location', 'New Location')

# Example: Replace values in 'Founded' column where the year is before 1900 with 'Old Founded Year'
data['Founded'] = data['Founded'].apply(lambda x: 'Old Founded Year' if pd.to_numeric(x, errors='coerce') < 1900 else x)

print("\n=== Data After Value Replacement ===")
print(data.head())
