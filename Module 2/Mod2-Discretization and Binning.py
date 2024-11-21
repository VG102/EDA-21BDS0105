import pandas as pd

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Bin 'Avg. Area Number of Rooms' into categories
bins = [0, 4, 6, 8, 10]
labels = ['Low', 'Medium', 'High', 'Luxury']
data['RoomCategory'] = pd.cut(data['Avg. Area Number of Rooms'], bins=bins, labels=labels, include_lowest=True)

print("\n=== Data After Binning ===")
print(data[['Avg. Area Number of Rooms', 'RoomCategory']].head())
