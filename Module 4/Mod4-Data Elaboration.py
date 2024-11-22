import pandas as pd

# Load the dataset
data = pd.read_csv('constituents.csv')

# Convert 'CIK' and 'Founded' columns to numeric, forcing errors to NaN
data['CIK'] = pd.to_numeric(data['CIK'], errors='coerce')
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')

# Check if the columns are now numeric and perform the calculation
if 'CIK' in data.columns and 'Founded' in data.columns:
    # Ensure there are no NaN values before calculation
    data['Price per Room'] = data['CIK'] / (data['Founded'] + 1)
    
    # Display the first few rows of the new column
    print("\n=== Data Elaboration: Price per Room ===")
    print(data[['CIK', 'Founded', 'Price per Room']].head())
else:
    print("Required columns 'CIK' and 'Founded' are missing.")
