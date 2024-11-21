import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100).reshape(-1, 1)  # Feature: Avg. Area Number of Rooms
y = 2 * x + 3 + np.random.normal(0, 1, size=(100, 1))  # Target: Price with some noise

# Create DataFrame
data = pd.DataFrame({'Avg. Area Number of Rooms': x.flatten(), 'Price': y.flatten()})

# Splitting data into training and testing sets
X = data[['Avg. Area Number of Rooms']]  # Features
y = data['Price']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Extract the coefficients (slope) and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Print the equation of the line
print(f"Equation of the line: y = {slope:.2f}x + {intercept:.2f}")

# Print evaluation metrics
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Visualizing the regression line
plt.scatter(X_test, y_test, color='blue', label='True values')
plt.plot(X_test, y_pred, color='red', label='Predicted line')
plt.title('Linear Regression: Predicted vs True values')
plt.xlabel('Avg. Area Number of Rooms')
plt.ylabel('Price')
plt.legend()
plt.show()
