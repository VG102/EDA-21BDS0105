import pandas as pd

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Data elaboration: Creating a new column for price per room
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    data['Price per Room'] = data['Price'] / data['Avg. Area Number of Rooms']
    print("\n=== Data Elaboration: Price per Room ===")
    print(data[['Price', 'Avg. Area Number of Rooms', 'Price per Room']].head())
else:
    print("Required columns 'Price' and 'Avg. Area Number of Rooms' are missing.")
