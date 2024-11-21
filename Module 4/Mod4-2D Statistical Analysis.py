import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# 2-D analysis: Scatter plot of 'Price' vs 'Avg. Area Number of Rooms'
if 'Price' in data.columns and 'Avg. Area Number of Rooms' in data.columns:
    sns.scatterplot(x=data['Avg. Area Number of Rooms'], y=data['Price'])
    plt.title('2-D Statistical Data Analysis: Price vs Rooms')
    plt.xlabel('Avg. Area Number of Rooms')
    plt.ylabel('Price')
    plt.show()
else:
    print("Required columns 'Price' and 'Avg. Area Number of Rooms' are missing.")
