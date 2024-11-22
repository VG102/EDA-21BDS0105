import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Clean the 'Founded' column by extracting the numeric year
data['Founded'] = data['Founded'].astype(str).str.extract(r'(\d{4})').astype(float)

# Convert 'Date added' to numeric (year as integer)
data['Date added'] = pd.to_datetime(data['Date added'], errors='coerce').dt.year

# Using 'Founded' and 'Date added' for Dimensionality Estimation
if 'Founded' in data.columns and 'Date added' in data.columns:
    features = data[['Founded', 'Date added']].dropna()

    # PCA to estimate intrinsic dimensionality
    pca = PCA()
    pca.fit(features)
    explained_variance = pca.explained_variance_ratio_

    # Determine the number of components to explain 95% variance
    cumulative_variance = np.cumsum(explained_variance)
    n_components = np.where(cumulative_variance >= 0.95)[0][0] + 1

    print(f"Intrinsic Dimensionality: {n_components} components are needed to explain 95% variance.")
else:
    print("Required columns 'Founded' and 'Date added' are missing.")
