import matplotlib.pyplot as plt
import numpy as np

# Data for pie chart
y = np.array([35, 25, 25, 15])  # Values for each slice
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]  # Labels for each slice
myexplode = [0.2, 0, 0, 0]  # Explode the first slice (Apples)

# Creating the pie chart
plt.figure(figsize=(8, 6))  # Set the figure size
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title('Fruit Distribution')  # Title of the pie chart

# Show the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
