import pandas as pd
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for clustering
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

    # Scale the data
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Spectral Clustering
    spectral = SpectralClustering(n_clusters=3, affinity='nearest_neighbors', random_state=0)
    labels = spectral.fit_predict(features_scaled)

    # Plot the clusters
    plt.scatter(features['Avg. Area Number of Rooms'], features['Price'], c=labels, cmap='viridis', alpha=0.7)
    plt.title('Spectral Clustering')
    plt.xlabel('Avg. Area Number of Rooms')
    plt.ylabel('Price')
    plt.show()
else:
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
