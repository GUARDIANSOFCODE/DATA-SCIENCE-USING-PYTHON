import matplotlib.pyplot as plt

# Sample data points (example)
ypoints = [60, 65, 70, 75, 80, 85, 90]

# Plot the same data with different line styles
plt.plot(ypoints, linestyle='dotted', label='Dotted Line')
plt.plot(ypoints, linestyle='dashed', label='Dashed Line')

# Add labels and title
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data")

# Display legend for clarity
plt.legend()

# Show the plot
plt.show()
