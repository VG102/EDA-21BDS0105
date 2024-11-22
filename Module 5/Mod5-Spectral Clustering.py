import pandas as pd
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# Creating a fixed dataset with three numeric columns
fixed_data = {
    'Feature1': [1.2, 2.5, 3.1, 4.6, 5.2, 6.3, 7.4, 8.1, 9.2, 10.5],
    'Feature2': [2.3, 3.7, 4.2, 5.6, 6.4, 7.8, 8.5, 9.1, 10.3, 11.7],
    'Feature3': [10.1, 20.2, 30.3, 40.4, 50.5, 60.6, 70.7, 80.8, 90.9, 100.1]
}

# Create a DataFrame from the fixed data
data = pd.DataFrame(fixed_data)

# Select numerical columns (excluding non-numeric data)
numeric_columns = data.select_dtypes(include=[np.number]).columns

# If there are enough numeric columns, proceed with clustering
if len(numeric_columns) > 1:  # Ensure at least two numeric columns for clustering
    features = data[numeric_columns].dropna()  # Drop rows with missing values

    # Scale the data
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Spectral Clustering
    spectral = SpectralClustering(n_clusters=3, affinity='nearest_neighbors', random_state=0)
    labels = spectral.fit_predict(features_scaled)

    # Plot the clusters
    plt.scatter(features[numeric_columns[0]], features[numeric_columns[1]], c=labels, cmap='viridis', alpha=0.7)
    plt.title('Spectral Clustering')
    plt.xlabel(numeric_columns[0])
    plt.ylabel(numeric_columns[1])
    plt.show()
else:
    print("Not enough numeric columns for clustering.")
