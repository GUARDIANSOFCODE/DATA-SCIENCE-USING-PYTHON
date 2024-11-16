import numpy as np

# Create a 2D NumPy array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [6, 7, 8]])

# Access the last row of the array
last_element = array[-1, :]

print("Last row:", last_element)
