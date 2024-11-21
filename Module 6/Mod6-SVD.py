import pandas as pd
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for SVD
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

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
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
