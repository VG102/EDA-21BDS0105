import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Split columns into numerical and categorical
numerical_data = data.select_dtypes(include=[np.number])
categorical_data = data.select_dtypes(exclude=[np.number])

# Print numerical and categorical columns
print("Numerical Columns:", numerical_data.columns.tolist())
print("Categorical Columns:", categorical_data.columns.tolist())

# Ensure there is at least one categorical column for plotting
if not categorical_data.empty:
    # Select the first categorical column for demonstration
    cat_column = categorical_data.columns[0]
    print(f"\nBar plot for the first categorical column: {cat_column}")

    # Create a bar plot for the selected column
    categorical_data[cat_column].value_counts().sort_index().plot(kind='bar')
    plt.title(f'Distribution of {cat_column}')
    plt.xlabel(cat_column)
    plt.ylabel('Frequency')
    plt.show()
else:
    print("No categorical columns available for plotting.")
