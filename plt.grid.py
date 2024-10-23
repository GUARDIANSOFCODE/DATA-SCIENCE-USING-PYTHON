import matplotlib.pyplot as plt

# Sample data points (example)
ypoints = [60, 65, 70, 75, 80, 85, 90]

# Plotting the data
plt.plot(ypoints, linestyle='dashed')

# Add labels and title
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data")

# Enable grid
plt.grid(True)

# Show the plot
plt.show()
