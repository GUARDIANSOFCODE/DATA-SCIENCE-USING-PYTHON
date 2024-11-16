import numpy as np

# Correct the array definition
array = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

# Get the last element of the array (last row)
last_element = array[-1, :]

# Print the last element
print("Last element:", last_element)
