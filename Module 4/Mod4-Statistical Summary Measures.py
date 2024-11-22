import pandas as pd

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Convert 'Founded' column to numeric (if it's in text form, handle it as a number)
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')

# Display summary statistics for numeric columns
print("\n=== Statistical Summary Measures ===")
print(data.describe())
