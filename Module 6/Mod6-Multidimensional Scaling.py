import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Using 'Avg. Area Number of Rooms' and 'Price' for MDS
if 'Avg. Area Number of Rooms' in data.columns and 'Price' in data.columns:
    features = data[['Avg. Area Number of Rooms', 'Price']].dropna()

    # Downsample the data (e.g., use 500 points)
    features_sampled = features.sample(500, random_state=0)

    # MDS
    mds = MDS(n_components=2, random_state=0)
    mds_components = mds.fit_transform(features_sampled)

    # Plot the MDS components
    plt.figure(figsize=(8, 6))
    plt.scatter(mds_components[:, 0], mds_components[:, 1], alpha=0.7)
    plt.title('Multidimensional Scaling (MDS)')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.show()
else:
    print("Required columns 'Avg. Area Number of Rooms' and 'Price' are missing.")
