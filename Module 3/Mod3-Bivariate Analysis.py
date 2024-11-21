import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Scatter plot for 'Avg. Area Number of Rooms' vs 'Price'
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['Avg. Area Number of Rooms'], y=data['Price'])
plt.title('Bivariate Analysis - Scatter Plot of Rooms vs Price')
plt.xlabel('Avg. Area Number of Rooms')
plt.ylabel('Price')
plt.show()

# Correlation coefficient between 'Avg. Area Number of Rooms' and 'Price'
correlation = data[['Avg. Area Number of Rooms', 'Price']].corr()
print("\n=== Bivariate Analysis: Correlation Between 'Rooms' and 'Price' ===")
print(correlation)

# Linear Regression Plot for 'Avg. Area Number of Rooms' vs 'Price'
sns.lmplot(x='Avg. Area Number of Rooms', y='Price', data=data)
plt.title('Bivariate Analysis - Linear Regression of Rooms vs Price')
plt.show()
