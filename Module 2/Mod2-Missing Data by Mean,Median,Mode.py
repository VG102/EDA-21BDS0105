import pandas as pd

# Load the dataset
data = pd.read_csv('constituents.csv')

# Fill missing 'Headquarters Location' with the most frequent value (mode)
data['Headquarters Location'] = data['Headquarters Location'].fillna(data['Headquarters Location'].mode()[0])

# Fill missing 'Founded' with the median (assuming it’s numeric or can be treated as such)
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')
data['Founded'] = data['Founded'].fillna(data['Founded'].median())

# Fill missing 'GICS Sector' with the most frequent value (mode)
data['GICS Sector'] = data['GICS Sector'].fillna(data['GICS Sector'].mode()[0])

print("\n=== Data After Imputation ===")
print(data.head())
