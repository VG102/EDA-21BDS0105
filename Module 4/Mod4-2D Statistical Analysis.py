import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('constituents.csv')

# 2-D analysis: Scatter plot of 'CIK' vs 'Founded' (or other columns as needed)
if 'CIK' in data.columns and 'Founded' in data.columns:
    sns.scatterplot(x=data['Founded'], y=data['CIK'])
    plt.title('2-D Statistical Data Analysis: CIK vs Founded Year')
    plt.xlabel('Founded Year')
    plt.ylabel('CIK')
    plt.show()
else:
    print("Required columns 'CIK' and 'Founded' are missing.")
