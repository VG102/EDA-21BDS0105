import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for Dimensionality Estimation
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

    # PCA to estimate intrinsic dimensionality
    pca = PCA()
    pca.fit(features)
    explained_variance = pca.explained_variance_ratio_

    # Determine the number of components to explain 95% variance
    cumulative_variance = np.cumsum(explained_variance)
    n_components = np.where(cumulative_variance >= 0.95)[0][0] + 1

    print(f"Intrinsic Dimensionality: {n_components} components are needed to explain 95% variance.")
else:
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
