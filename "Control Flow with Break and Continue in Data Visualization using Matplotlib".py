# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data for visualization
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # y is the sine of x

# Initialize a list to store filtered data
filtered_x = []
filtered_y = [].   

# Loop through the data to apply conditions with break and continue
for i in range(len(x)):
    if y[i] < 0:  # Skip negative y values using 'continue'
        continue
    if x[i] > 8:  # Break the loop if x is greater than 8
        break
    
    # Add the valid data points to the filtered lists
    filtered_x.append(x[i])
    filtered_y.append(y[i])

# Data visualization with filtered data
plt.figure(figsize=(10, 6))

# Line plot of the filtered data
plt.plot(filtered_x, filtered_y, label='Filtered Sine Wave', color='b', linewidth=2)

# Title and labels
plt.title('Filtered Sine Wave with Break and Continue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
