import pandas as pd

# Load the dataset
data = pd.read_csv('constituents.csv')

# Contingency table: Example using categorical columns
if 'Headquarters Location' in data.columns:
    # Assuming 'Headquarters Location' is in the format 'City, State' or similar
    data['City'] = data['Headquarters Location'].apply(lambda x: x.split(',')[0].strip() if ',' in x else 'Unknown')
    
    # Creating a contingency table for 'City' vs 'GICS Sector'
    contingency_table = pd.crosstab(data['City'], data['GICS Sector'])
    
    print("\n=== Contingency Table ===")
    print(contingency_table)
else:
    print("The column 'Headquarters Location' is missing.")
