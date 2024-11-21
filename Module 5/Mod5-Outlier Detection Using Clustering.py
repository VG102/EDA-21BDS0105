import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for clustering
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

    # DBSCAN for outlier detection
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(features)

    # Plot results
    plt.scatter(features['Avg. Area Number of Rooms'], features['Price'], c=labels, cmap='viridis', alpha=0.7)
    plt.title('Outlier Detection Using DBSCAN')
    plt.xlabel('Avg. Area Number of Rooms')
    plt.ylabel('Price')
    plt.show()
else:
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
