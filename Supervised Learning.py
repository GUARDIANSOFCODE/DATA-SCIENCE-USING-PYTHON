# Importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset
data = {
    'SquareFeet': [850, 900, 1200, 1500, 1800],
    'Price': [250000, 270000, 340000, 400000, 500000]
}
df = pd.DataFrame(data)

# Features and target
X = df[['SquareFeet']]
y = df['Price']

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
print("Predicted Prices:", y_pred)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
