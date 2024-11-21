import pandas as pd
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for Factor Analysis
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

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
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
