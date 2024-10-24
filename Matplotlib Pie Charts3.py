import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
y = np.array([35, 25, 25, 15])  # Values for each slice
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]  # Labels for each slice

# Creating the pie chart
plt.figure(figsize=(8, 6))  # Set the figure size for better visibility
plt.pie(y, labels=mylabels, autopct='%1.1f%%', startangle=140, shadow=True)

# Adding a legend with a title
plt.legend(title="Four Fruits:", loc="upper right", fontsize='medium')

# Adding a title
plt.title('Fruit Distribution Pie Chart')

# Show the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
