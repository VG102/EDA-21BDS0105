import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Pairplot for multivariate (n-D) analysis
numeric_columns = data.select_dtypes(include=['number']).columns
if len(numeric_columns) >= 2:
    sns.pairplot(data[numeric_columns])
    plt.suptitle('n-D Statistical Data Analysis: Pairplot', y=1.02)
    plt.show()
else:
    print("The dataset does not have enough numeric columns for n-D analysis.")
