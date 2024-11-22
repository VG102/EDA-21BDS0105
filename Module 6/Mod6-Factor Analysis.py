import pandas as pd
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Clean the 'Founded' column by extracting the numeric year
data['Founded'] = data['Founded'].astype(str).str.extract(r'(\d{4})').astype(float)

# Convert 'Date added' to numeric (year as integer)
data['Date added'] = pd.to_datetime(data['Date added'], errors='coerce').dt.year

# Using 'Founded' and 'Date added' for Factor Analysis
if 'Founded' in data.columns and 'Date added' in data.columns:
    features = data[['Founded', 'Date added']].dropna()

    # Factor Analysis
    factor = FactorAnalysis(n_components=2)
    factor_components = factor.fit_transform(features)

    # Plot the Factor components
    plt.figure(figsize=(8, 6))
    plt.scatter(factor_components[:, 0], factor_components[:, 1], alpha=0.7)
    plt.title('Factor Analysis - First Two Components')
    plt.xlabel('Factor 1')
    plt.ylabel('Factor 2')
    plt.show()
else:
    print("Required columns 'Founded' and 'Date added' are missing.")
