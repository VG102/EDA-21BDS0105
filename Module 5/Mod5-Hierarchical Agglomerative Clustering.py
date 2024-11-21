import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for clustering
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

    # Downsample the data to 1000 points
    features_sampled = features.sample(1000, random_state=0)

    # Compute linkage for hierarchical clustering
    Z = linkage(features_sampled, method='ward')

    # Dendrogram
    plt.figure(figsize=(10, 7))
    dendrogram(Z)
    plt.title('Hierarchical Agglomerative Clustering (Downsampled)')
    plt.xlabel('Index')
    plt.ylabel('Distance')
    plt.show()
else:
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
