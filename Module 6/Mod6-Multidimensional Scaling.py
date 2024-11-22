import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Clean the 'Founded' column by extracting the numeric year
data['Founded'] = data['Founded'].astype(str).str.extract(r'(\d{4})').astype(float)

# Convert 'Date added' to numeric (year as integer)
data['Date added'] = pd.to_datetime(data['Date added'], errors='coerce').dt.year

# Using 'Founded' and 'Date added' for MDS
if 'Founded' in data.columns and 'Date added' in data.columns:
    features = data[['Founded', 'Date added']].dropna()

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
    print("Required columns 'Founded' and 'Date added' are missing.")
