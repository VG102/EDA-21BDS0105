import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Clean the 'Founded' column to extract numeric values (if necessary)
if 'Founded' in data.columns:
    # Extract numeric year from any text like '2013 (1888)'
    data['Founded'] = data['Founded'].str.extract(r'(\d{4})').astype(float)

    # Drop rows where 'Founded' is NaN
    features = data[['Founded']].dropna()

    # Downsample the data to 1000 points (if there are enough rows)
    if len(features) >= 1000:
        features_sampled = features.sample(1000, random_state=0)
    else:
        features_sampled = features

    # List of linkage methods to compare
    linkage_methods = ['single', 'complete', 'average', 'ward']
    
    # Plot dendrograms for each method
    plt.figure(figsize=(15, 10))
    
    for i, method in enumerate(linkage_methods, 1):
        # Compute linkage for the current method
        Z = linkage(features_sampled, method=method)
        
        # Create a subplot for each dendrogram
        plt.subplot(2, 2, i)
        dendrogram(Z)
        plt.title(f'Hierarchical Clustering ({method.capitalize()})')
        plt.xlabel('Index')
        plt.ylabel('Distance')
    
    plt.tight_layout()
    plt.show()

else:
    print("The 'Founded' column is missing.")
