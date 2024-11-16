import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create a simple line plot
plt.plot(x, y)

# Add a title with customized font size and color
plt.title('Customized Line Plot', fontsize=16, color='blue')

# Add labels with customized font size and color
plt.xlabel('X-Axis Label', fontsize=12, color='green')
plt.ylabel('Y-Axis Label', fontsize=12, color='red')

# Display the plot
plt.show()
