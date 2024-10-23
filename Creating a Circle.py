import numpy as np
import matplotlib.pyplot as plt

# Create a circle using parametric equations
theta = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2π
x = np.cos(theta)  # x = cos(θ)
y = np.sin(theta)  # y = sin(θ)

# Plot the circle
plt.figure()
plt.plot(x, y, marker='o')  # Using 'o' for circular markers
plt.title("Circle Using Parametric Equations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')  # Equal aspect ratio for x and y axes
plt.grid()
plt.show()
