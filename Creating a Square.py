import matplotlib.pyplot as plt

# Define the points for a square
x = [1, 1, -1, -1, 1]  # Close the square by returning to the starting point
y = [1, -1, -1, 1, 1]  # Close the square by returning to the starting point

# Plot the square
plt.figure()
plt.plot(x, y, marker='s')  # Using 's' for square markers
plt.title("Square Using Defined Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')  # Equal aspect ratio for x and y axes
plt.grid()
plt.show()
