import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Dot chart for 'Price'
if 'Price' in data.columns:
    plt.plot(data['Price'], 'o', alpha=0.7)
    plt.title('Dot Chart: Price')
    plt.xlabel('Index')
    plt.ylabel('Price')
    plt.show()
else:
    print("The column 'Price' is missing.")
