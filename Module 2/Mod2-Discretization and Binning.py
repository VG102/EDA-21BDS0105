import pandas as pd

# Load the dataset
data = pd.read_csv('constituents.csv')

# Ensure relevant column exists, and extract numeric values from 'Founded'
data['Founded_numeric'] = pd.to_numeric(data['Founded'].str.extract(r'(\d{4})')[0], errors='coerce')

# Bin 'Founded_numeric' into categories
bins = [0, 1900, 1950, 2000, 2024]  # Adjust the bins as per the data
labels = ['Early', 'Mid', 'Late', 'Modern']
data['FoundedCategory'] = pd.cut(data['Founded_numeric'], bins=bins, labels=labels, include_lowest=True)

print("\n=== Data After Binning ===")
print(data[['Founded_numeric', 'FoundedCategory']].head())
