import matplotlib.pyplot as plt

# Sample data points (example)
ypoints = [60, 65, 70, 75, 80, 85, 90]

# Plotting the data
plt.plot(ypoints, linestyle='dashed')

# Define font style
font1 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# Add title with custom font and position it on the left
plt.title("Sports Watch Data", fontdict=font1, loc='left')

# Add labels
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

# Show the plot
plt.show()
