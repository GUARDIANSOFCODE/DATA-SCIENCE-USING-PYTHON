import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for the plots
plt.figure(figsize=(8, 6))

# Plot 1:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st plot
plt.plot(x1, y1, marker='o', color='b', label='Plot 1')
plt.title('Plot 1: Y-Coordinates')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.legend()
plt.grid()

# Plot 2:
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd plot
plt.plot(x2, y2, marker='s', color='r', label='Plot 2')
plt.title('Plot 2: Y-Coordinates')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.legend()
plt.grid()

# Show the plots
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
