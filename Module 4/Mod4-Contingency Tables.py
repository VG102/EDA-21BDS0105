import pandas as pd

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Contingency table: Example using categorical columns
if 'Address' in data.columns:
    data['City'] = data['Address'].apply(lambda x: x.split(',')[1].strip() if ',' in x else 'Unknown')
    contingency_table = pd.crosstab(data['City'], data['Avg. Area Number of Bedrooms'])
    print("\n=== Contingency Table ===")
    print(contingency_table)
else:
    print("The column 'Address' is missing.")
