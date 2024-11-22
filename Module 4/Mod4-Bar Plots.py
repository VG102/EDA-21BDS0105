import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('constituents.csv')

# Bar plot for 'GICS Sector' (or other categorical columns)
if 'GICS Sector' in data.columns:
    data['GICS Sector'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Bar Plot: GICS Sector Distribution')
    plt.xlabel('GICS Sector')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The column 'GICS Sector' is missing.")
