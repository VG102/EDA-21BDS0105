import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('constituents.csv')

# Ensure 'Founded' is numeric (in case it's not)
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')

# 1-D analysis: Histogram for 'Founded'
if 'Founded' in data.columns:
    plt.hist(data['Founded'], bins=20, edgecolor='black')
    plt.title('1-D Statistical Data Analysis: Histogram of Founded Year')
    plt.xlabel('Founded Year')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The column 'Founded' is missing.")
