import pandas as pd

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Fill missing 'Price' with the mean value
data['Price'] = data['Price'].fillna(data['Price'].mean())

# Fill missing 'Avg. Area Number of Rooms' with the median
data['Avg. Area Number of Rooms'] = data['Avg. Area Number of Rooms'].fillna(data['Avg. Area Number of Rooms'].median())

# Fill missing 'Address' with the most frequent value (mode)
data['Address'] = data['Address'].fillna(data['Address'].mode()[0])

print("\n=== Data After Imputation ===")
print(data.head())
