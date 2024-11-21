import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler

# Create a fixed dataset of points (for example, 10 points in a 2D space)
fixed_data = np.array([[1, 2],
                       [2, 3],
                       [3, 4],
                       [5, 6],
                       [8, 7],
                       [9, 10],
                       [10, 12],
                       [13, 15],
                       [15, 16],
                       [18, 20]])

# Optionally, scale the data to standardize the features (important if the scale varies)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(fixed_data)

# Generate dendrograms for different linkage methods
linkage_methods = ['single', 'complete', 'average', 'ward']

plt.figure(figsize=(16, 12))

for i, method in enumerate(linkage_methods, 1):
    plt.subplot(2, 2, i)
    Z = linkage(scaled_data, method=method)
    dendrogram(Z)
    plt.title(f"Dendrogram ({method.capitalize()} Linkage)")
    plt.xlabel("Sample Index")
    plt.ylabel("Distance")

plt.tight_layout()
plt.show()
