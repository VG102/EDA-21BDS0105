import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for clustering
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

    # Gaussian Mixture Model
    gmm = GaussianMixture(n_components=3, random_state=0)
    gmm_labels = gmm.fit_predict(features)

    # Plot the clusters
    plt.scatter(features['Avg. Area Number of Rooms'], features['Price'], c=gmm_labels, cmap='viridis', alpha=0.7)
    plt.title('Model-Based Clustering (GMM)')
    plt.xlabel('Avg. Area Number of Rooms')
    plt.ylabel('Price')
    plt.show()
else:
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
