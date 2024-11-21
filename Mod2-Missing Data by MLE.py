import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Load the dataset
data = pd.read_csv('housing_data.csv')

# Initialize the MLE imputer
imputer = IterativeImputer(max_iter=10, random_state=0)

# Perform imputation on the numeric columns
numeric_cols = data.select_dtypes(include=['number']).columns
data[numeric_cols] = imputer.fit_transform(data[numeric_cols])

print("\n=== Data After MLE Imputation ===")
print(data.head())
