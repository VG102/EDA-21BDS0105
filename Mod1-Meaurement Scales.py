import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Verify column names
print("Columns in dataset:", data.columns)

# Create a categorical column by binning 'Avg. Area Number of Rooms'
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    # Bin the 'Avg. Area Number of Rooms' into categories
    bins = [0, 4, 6, 8, 10]
    labels = ['Low', 'Medium', 'High', 'Luxury']
    data['RoomCategory'] = pd.cut(data['Avg. Area Number of Rooms'], bins=bins, labels=labels, include_lowest=True)

    print("\n=== Head of 'RoomCategory' Column ===")
    print(data[['Avg. Area Number of Rooms', 'RoomCategory']].head())

    # Box plot for 'Price' across 'RoomCategory'
    sns.boxplot(x='RoomCategory', y='Price', data=data)
    plt.title('Price by Room Category')
    plt.xlabel('Room Category')
    plt.ylabel('Price')
    plt.show()
else:
    print("The dataset does not contain the required columns 'Avg. Area Number of Rooms' and 'Price'.")
