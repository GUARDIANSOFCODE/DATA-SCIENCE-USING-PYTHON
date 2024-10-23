import matplotlib.pyplot as plt
import numpy as np

# Create the first plot
x1 = np.array([0, 1, 2, 3])  # X values for the first plot
y1 = np.array([3, 8, 1, 10])  # Y values for the first plot

plt.subplot(1, 2, 1)  # Specifies a 1x2 grid, and this is the first plot
plt.plot(x1, y1, marker='o')  # Plot with circular markers
plt.title("First Plot")  # Title for the first subplot
plt.xlabel("X-axis")  # X-axis label
plt.ylabel("Y-axis")  # Y-axis label
plt.grid()  # Add grid lines

# Create the second plot
x2 = np.array([0, 1, 2, 3])  # X values for the second plot
y2 = np.array([10, 20, 30, 40])  # Y values for the second plot

plt.subplot(1, 2, 2)  # Specifies a 1x2 grid, and this is the second plot
plt.plot(x2, y2, marker='s', color='orange')  # Plot with square markers
plt.title("Second Plot")  # Title for the second subplot
plt.xlabel("X-axis")  # X-axis label
plt.ylabel("Y-axis")  # Y-axis label
plt.grid()  # Add grid lines

# Show all plots
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plots
