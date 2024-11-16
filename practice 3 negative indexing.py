import numpy as np

# Example array
array = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

# Accessing the last two rows of the array (all columns)
last_two_rows = array[-2:, :]

# Print the result
print("last_two_rows:", last_two_rows)
