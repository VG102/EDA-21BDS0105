import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Create a fixed dataset with x and y values (for demonstration purposes)
# Here, x and y represent features like 'Avg. Area Number of Rooms' and 'Price'
data = {
    'x': [1, 2, 3, 4, 5, 6],
    'y': [100, 200, 300, 400, 500, 600]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features (x and y values)
features = df[['x', 'y']]

# Standardizing the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# PCA
pca = PCA(n_components=2)
pca_components = pca.fit_transform(features_scaled)

# Extract the principal components (PC1 and PC2)
pc1 = pca_components[:, 0]
pc2 = pca_components[:, 1]

# Print the values of x, y, pc1, and pc2
print("\n=== PCA - Values of x, y, pc1, pc2 ===")
for i in range(len(features)):
    print(f"x: {df.iloc[i, 0]}, y: {df.iloc[i, 1]}, pc1: {pc1[i]}, pc2: {pc2[i]}")

# Plot the first two principal components
plt.figure(figsize=(8, 6))
plt.scatter(pc1, pc2, alpha=0.7)
plt.title('PCA - First Two Principal Components')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# Print explained variance ratio
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)
