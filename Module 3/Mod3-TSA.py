import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Ensure the dataset has a 'Date' column. Generate one if missing.
if 'Date' not in data.columns:
    data['Date'] = pd.date_range(start='2020-01-01', periods=len(data), freq='D')

# Convert 'Date' to datetime and set it as the index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Select only numeric columns for resampling
numeric_data = data.select_dtypes(include=['number'])

# Monthly average
monthly_avg = numeric_data.resample('MS').mean()

# Plot the monthly average for the 'Price' column
if 'Price' in monthly_avg.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_avg.index, monthly_avg['Price'], label='Monthly Average Price')
    plt.title('Time Series Analysis - Monthly Average Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
else:
    print("The 'Price' column is not available for plotting.")
