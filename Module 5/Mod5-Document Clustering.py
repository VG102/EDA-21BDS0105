import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Assuming the 'Security' column contains textual data
if 'Security' in data.columns:
    # Vectorize the textual data
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data['Security'].dropna())  # Dropping NaN values

    # KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    labels = kmeans.fit_predict(X)

    # Add cluster labels to the dataset
    data['Cluster'] = labels

    print("\n=== Document Clustering Results ===")
    print(data[['Security', 'Cluster']].head())
else:
    print("The column 'Security' is missing.")
