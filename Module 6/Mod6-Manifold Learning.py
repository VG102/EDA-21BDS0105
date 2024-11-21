import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import Isomap
from sklearn.decomposition import PCA

# Load a sample dataset (Digits dataset in this case)
digits = datasets.load_digits()
X = digits.data
y = digits.target

# Apply Isomap for manifold learning
n_neighbors = 10  # Number of neighbors
n_components = 2  # Dimensionality of the embedding

isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
X_isomap = isomap.fit_transform(X)

# Apply PCA for comparison (optional)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Isomap plot
axes[0].scatter(X_isomap[:, 0], X_isomap[:, 1], c=y, cmap='jet', edgecolor='k')
axes[0].set_title('Isomap')
axes[0].set_xlabel('Component 1')
axes[0].set_ylabel('Component 2')

# PCA plot for comparison
axes[1].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='jet', edgecolor='k')
axes[1].set_title('PCA')
axes[1].set_xlabel('Component 1')
axes[1].set_ylabel('Component 2')

plt.tight_layout()
plt.show()
