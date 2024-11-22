import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('constituents.csv')

# Preprocess 'Founded' to extract numeric year (using raw string for regex)
data['Founded'] = data['Founded'].str.extract(r'(\d{4})').astype(float)

# Ensure 'CIK' is numeric
data['CIK'] = pd.to_numeric(data['CIK'], errors='coerce')  # Coerce errors to NaN

# Scatter plot for 'Founded' vs 'CIK'
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['Founded'], y=data['CIK'])
plt.title('Bivariate Analysis - Scatter Plot of Founded vs CIK')
plt.xlabel('Founded')
plt.ylabel('CIK')
plt.show()

# Correlation coefficient between 'Founded' and 'CIK'
correlation = data[['Founded', 'CIK']].corr()
print("\n=== Bivariate Analysis: Correlation Between 'Founded' and 'CIK' ===")
print(correlation)

# Linear Regression Plot for 'Founded' vs 'CIK'
sns.lmplot(x='Founded', y='CIK', data=data)
plt.title('Bivariate Analysis - Linear Regression of Founded vs CIK')
plt.show()
