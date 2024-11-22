import pandas as pd
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Convert 'Founded' column to numeric (if it's in text form, handle it as a number)
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')

# Scatter plot: 'Founded' vs 'CIK' (or any other numeric column)
if 'Founded' in data.columns and 'CIK' in data.columns:
    plt.scatter(data['Founded'], data['CIK'], alpha=0.7)
    plt.title('Scatter Plot: Founded Year vs CIK')
    plt.xlabel('Founded Year')
    plt.ylabel('CIK')
    plt.show()
else:
    print("Required columns 'Founded' and 'CIK' are missing.")
