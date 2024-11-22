import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('constituents.csv')

# Verify column names
print("Columns in dataset:", data.columns)

# Replace 'Avg. Area Number of Rooms' and 'Price' with appropriate numeric columns from constituents.csv
if 'CIK' in data.columns and 'Founded' in data.columns:
    # Bin the 'CIK' column into categories
    bins = [0, 50000, 100000, 150000, 200000]
    labels = ['Low', 'Medium', 'High', 'Luxury']
    data['CIK_Category'] = pd.cut(data['CIK'], bins=bins, labels=labels, include_lowest=True)

    print("\n=== Head of 'CIK_Category' Column ===")
    print(data[['CIK', 'CIK_Category']].head())

    # Box plot for 'Founded' across 'CIK_Category'
    sns.boxplot(x='CIK_Category', y='Founded', data=data)
    plt.title('Founded Year by CIK Category')
    plt.xlabel('CIK Category')
    plt.ylabel('Founded Year')
    plt.show()
else:
    print("The dataset does not contain the required columns 'CIK' and 'Founded'.")
