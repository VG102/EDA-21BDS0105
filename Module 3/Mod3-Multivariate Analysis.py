import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('constituents.csv')

# Ensure 'Founded' is numeric (if it's a year, this should work fine)
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')

# Check the columns to ensure the correct ones are being used
print("Columns in the dataset:", data.columns)

# Pairplot to visualize relationships between multiple variables
# Use only numeric columns for the pairplot
numeric_cols = data.select_dtypes(include=['number']).columns
sns.pairplot(data[numeric_cols])
plt.suptitle('Multivariate Analysis - Pairplot', y=1.02)
plt.show()

# Heatmap of correlations among multiple variables
correlation_matrix = data[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Multivariate Analysis - Correlation Heatmap')
plt.show()

# Multiple Linear Regression Model
import statsmodels.api as sm

# Use appropriate numeric columns for regression
X = data[['Founded', 'CIK']]  # Independent variables
y = data['Founded']  # Dependent variable (target)

# Add a constant for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Print the regression summary
print("\n=== Multivariate Analysis: Multiple Linear Regression Summary ===")
print(model.summary())
