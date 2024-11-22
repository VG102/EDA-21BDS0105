import pandas as pd
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Clean the 'Founded' column by extracting the numeric year
data['Founded'] = data['Founded'].astype(str).str.extract(r'(\d{4})').astype(float)

# Convert 'Date added' to numeric (year as integer)
data['Date added'] = pd.to_datetime(data['Date added'], errors='coerce').dt.year

# Using 'Founded' and 'Date added' for SVD
if 'Founded' in data.columns and 'Date added' in data.columns:
    features = data[['Founded', 'Date added']].dropna()

    # SVD
    svd = TruncatedSVD(n_components=2)
    svd_components = svd.fit_transform(features)

    # Plot the SVD components
    plt.figure(figsize=(8, 6))
    plt.scatter(svd_components[:, 0], svd_components[:, 1], alpha=0.7)
    plt.title('SVD - First Two Components')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.show()

    print("\nExplained Variance Ratio:", svd.explained_variance_ratio_)
else:
    print("Required columns 'Founded' and 'Date added' are missing.")
