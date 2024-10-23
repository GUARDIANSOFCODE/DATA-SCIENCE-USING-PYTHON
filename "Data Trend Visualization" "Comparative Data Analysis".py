import matplotlib.pyplot as plt
import numpy as np

# Sample data for demonstration
x = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([10, 20, 30, 40])

# Create a figure for subplots
plt.figure()

# First subplot: 1 row, 2 columns, first plot
plt.subplot(1, 2, 1)  # Specifies the grid layout (1 row, 2 columns), and this is the first subplot
plt.plot(x, y1, marker='o')  # Example plot for the first subplot
plt.title("Data Trend Visualization")  # Title for the first subplot
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Second subplot: 1 row, 2 columns, second plot
plt.subplot(1, 2, 2)  # Specifies the grid layout (1 row, 2 columns), and this is the second subplot
plt.plot(x, y2, marker='s', color='orange')  # Example plot for the second subplot
plt.title("Comparative Data Analysis")  # Title for the second subplot
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the combined plots
plt.tight_layout()  # Adjust layout for better spacing
plt.show()
