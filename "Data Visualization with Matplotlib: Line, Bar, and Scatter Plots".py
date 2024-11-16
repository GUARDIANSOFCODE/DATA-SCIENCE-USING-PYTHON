# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Data preparation
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # y is the sine of x

# Create the figure
plt.figure(figsize=(12, 6))  # Set the figure size

# Add a title for the whole figure
plt.suptitle('Various Types of Visualizations', fontsize=16, fontweight='bold')

# Line Plot
plt.subplot(1, 3, 1)  # Create a subplot (1 row, 3 columns, 1st plot)
plt.plot(x, y, label='Sine Wave', color='b', linewidth=2)  # Line plot
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

# Bar Plot
y_bar = np.random.randint(1, 10, 5)  # Random data for bar chart
x_bar = ['A', 'B', 'C', 'D', 'E']  # Categories for the bars

plt.subplot(1, 3, 2)  # 2nd plot
plt.bar(x_bar, y_bar, color='g')  # Bar plot
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True)

# Scatter Plot
y_scatter = np.random.rand(50)  # Random y values for scatter plot

plt.subplot(1, 3, 3)  # 3rd plot
plt.scatter(x[:50], y_scatter, color='r', marker='o')  # Scatter plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Adjust layout
plt.tight_layout()  # Adjust spacing between plots

# Show the figure
plt.show()
