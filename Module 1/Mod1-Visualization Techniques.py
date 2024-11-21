import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Check the columns
print("Columns in dataset:", data.columns)

# Ensure relevant columns exist
if 'Price' in data.columns and 'Avg. Area Number of Rooms' in data.columns:
    # Histogram for 'Price'
    data['Price'].plot(kind='hist', bins=20, edgecolor='black')
    plt.title('Histogram of Price')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

    # Linear regression plot: 'Avg. Area Number of Rooms' vs 'Price'
    sns.lmplot(x='Avg. Area Number of Rooms', y='Price', data=data, line_kws={'color': 'red'})
    plt.title('Avg. Area Number of Rooms vs Price with Linear Fit')
    plt.show()

    # Correlation Matrix for numerical columns
    numerical_data = data.select_dtypes(include=['number'])
    correlation_matrix = numerical_data.corr()

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
else:
    print("The dataset does not contain the required columns 'Price' or 'Avg. Area Number of Rooms'.")
