import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('constituents.csv')

# Convert 'Founded' to numeric (if it's a year, this should work fine)
data['Founded'] = pd.to_numeric(data['Founded'], errors='coerce')

# Handle missing values: Drop rows with NaN values or fill them with a default value
data = data.dropna(subset=['Founded', 'CIK'])  # Drop rows where 'Founded' or 'CIK' is NaN
# Alternatively, fill NaN with mean (if you prefer that approach)
# data['Founded'].fillna(data['Founded'].mean(), inplace=True)
# data['CIK'].fillna(data['CIK'].mean(), inplace=True)

# Check for any infinite or NaN values
if data[['Founded', 'CIK']].isnull().any().any():
    print("There are still missing values.")
else:
    print("No missing values in 'Founded' or 'CIK' columns.")

# Ensure there are no infinite values
if (data[['Founded', 'CIK']] == float('inf')).any().any():
    print("There are infinite values in 'Founded' or 'CIK'.")
else:
    print("No infinite values in 'Founded' or 'CIK' columns.")

# Pairplot to visualize relationships between multiple variables
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

# Ensure 'CIK' is numeric (if needed)
data['CIK'] = pd.to_numeric(data['CIK'], errors='coerce')

# Define independent and dependent variables
X = data[['Founded', 'CIK']]  # Independent variables
y = data['Founded']  # Dependent variable (target)

# Add a constant for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Print the regression summary
print("\n=== Multivariate Analysis: Multiple Linear Regression Summary ===")
print(model.summary())
