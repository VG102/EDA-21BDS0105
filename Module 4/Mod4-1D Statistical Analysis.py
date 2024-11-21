import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# 1-D analysis: Histogram for 'Price'
if 'Price' in data.columns:
    plt.hist(data['Price'], bins=20, edgecolor='black')
    plt.title('1-D Statistical Data Analysis: Histogram of Price')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The column 'Price' is missing.")
