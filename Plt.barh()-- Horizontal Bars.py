import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.array(["A", "B", "C", "D"])  # Categories
y = np.array([3, 8, 1, 10])          # Values

# Creating the horizontal bar chart
plt.barh(x, y, height=0.4, color='skyblue')  # Added color for visual appeal

# Adding labels and title
plt.xlabel('Values')                      # X-axis label
plt.ylabel('Categories')                  # Y-axis label
plt.title('Horizontal Bar Chart Example') # Title of the chart

# Show the plot
plt.show()
