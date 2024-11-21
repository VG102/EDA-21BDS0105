import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Pairplot to visualize relationships between multiple variables
sns.pairplot(data[['Avg. Area Number of Rooms', 'Price', 'Area Population']])
plt.suptitle('Multivariate Analysis - Pairplot', y=1.02)
plt.show()

# Heatmap of correlations among multiple variables
correlation_matrix = data[['Avg. Area Number of Rooms', 'Price', 'Area Population']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Multivariate Analysis - Correlation Heatmap')
plt.show()

# Multiple Linear Regression Model
import statsmodels.api as sm

X = data[['Avg. Area Number of Rooms', 'Area Population']]
y = data['Price']

# Add a constant for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()
print("\n=== Multivariate Analysis: Multiple Linear Regression Summary ===")
print(model.summary())
