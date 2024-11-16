# Importing necessary libraries
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data: House sizes (X) and corresponding prices (y)
X = np.array([[500], [1000], [1500], [2000], [2500]])  # House sizes in square feet
y = np.array([100, 200, 300, 400, 500])  # Prices in thousands

# Creating and training the model
model = LinearRegression()
model.fit(X, y)

# Predicting the price of a house with 1800 square feet
new_house = np.array([[1800]])
predicted_price = model.predict(new_house)
print(f"Predicted price for a 1800 sqft house: ${predicted_price[0]}k")
