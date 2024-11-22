import pandas as pd
from sklearn.preprocessing import StandardScaler
from minisom import MiniSom
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Clean the 'Founded' column by extracting the numeric year
data['Founded'] = data['Founded'].astype(str).str.extract(r'(\d{4})').astype(float)

# Convert 'Date added' to numeric (year as integer)
data['Date added'] = pd.to_datetime(data['Date added'], errors='coerce').dt.year

# Using 'Founded' and 'Date added' for SOM
if 'Founded' in data.columns and 'Date added' in data.columns:
    features = data[['Founded', 'Date added']].dropna()

    # Scale the features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # SOM: 10x10 grid for the Self-Organizing Map
    som = MiniSom(x=10, y=10, input_len=2, sigma=1.0, learning_rate=0.5)
    som.random_weights_init(features_scaled)
    som.train_random(features_scaled, num_iteration=100)

    # Visualizing the SOM
    plt.figure(figsize=(8, 6))
    for x in range(10):
        for y in range(10):
            plt.text(x, y, f'{x},{y}', color='black', ha='center', va='center')
    plt.imshow(som.distance_map().T, cmap='coolwarm', origin='lower')
    plt.title('Self-Organizing Map')
    plt.show()
else:
    print("Required columns 'Founded' and 'Date added' are missing.")
