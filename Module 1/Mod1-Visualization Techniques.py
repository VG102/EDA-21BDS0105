import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('constituents.csv')

# Check the columns
print("Columns in dataset:", data.columns)

# Ensure relevant columns exist
if 'CIK' in data.columns and 'Founded' in data.columns:
    # Extract numeric values from 'Founded' and handle invalid formats
    data['Founded_numeric'] = pd.to_numeric(data['Founded'].str.extract(r'(\d{4})')[0], errors='coerce')

    # Drop rows with missing or invalid 'Founded' values
    data = data.dropna(subset=['Founded_numeric'])

    # Histogram for 'CIK'
    data['CIK'].plot(kind='hist', bins=20, edgecolor='black')
    plt.title('Histogram of CIK')
    plt.xlabel('CIK')
    plt.ylabel('Frequency')
    plt.show()

    # Linear regression plot: 'Founded_numeric' vs 'CIK'
    sns.lmplot(x='Founded_numeric', y='CIK', data=data, line_kws={'color': 'red'})
    plt.title('Founded (Numeric) vs CIK with Linear Fit')
    plt.show()

    # Correlation Matrix for numerical columns
    numerical_data = data.select_dtypes(include=['number'])
    correlation_matrix = numerical_data.corr()

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
else:
    print("The dataset does not contain the required columns 'CIK' or 'Founded'.")
