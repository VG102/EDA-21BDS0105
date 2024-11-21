import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Assuming the 'Address' column contains textual data
if 'Address' in data.columns:
    # Vectorize the textual data
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['Address'].dropna())

    # KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    labels = kmeans.fit_predict(X)

    # Add cluster labels to the dataset
    data['Cluster'] = labels

    print("\n=== Document Clustering Results ===")
    print(data[['Address', 'Cluster']].head())
else:
    print("The column 'Address' is missing.")
