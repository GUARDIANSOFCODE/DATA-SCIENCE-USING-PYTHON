import matplotlib.pyplot as plt
import numpy as np
 
# Day one, the age and speed of 11 cars:
x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77])

# Day two, the age and speed of 13 cars:
x2 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7])
y2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91])

# Create scatter plots for both datasets
plt.scatter(x1, y1, color='blue', label='Day One')
plt.scatter(x2, y2, color='orange', label='Day Two')

# Add labels and a legend for clarity
plt.xlabel('Age')
plt.ylabel('Speed')
plt.title('Comparison of Car Age and Speed on Two Different Days')
plt.legend()

# Display the plot
plt.show()
