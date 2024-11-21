import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Bar plot for 'Avg. Area Number of Bedrooms'
if 'Avg. Area Number of Bedrooms' in data.columns:
    data['Avg. Area Number of Bedrooms'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Bar Plot: Number of Bedrooms')
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The column 'Avg. Area Number of Bedrooms' is missing.")
