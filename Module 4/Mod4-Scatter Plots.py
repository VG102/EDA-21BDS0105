import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Scatter plot: 'Avg. Area Number of Rooms' vs 'Price'
if 'Price' in data.columns and 'Avg. Area Number of Rooms' in data.columns:
    plt.scatter(data['Avg. Area Number of Rooms'], data['Price'], alpha=0.7)
    plt.title('Scatter Plot: Price vs Rooms')
    plt.xlabel('Avg. Area Number of Rooms')
    plt.ylabel('Price')
    plt.show()
else:
    print("Required columns 'Price' and 'Avg. Area Number of Rooms' are missing.")
