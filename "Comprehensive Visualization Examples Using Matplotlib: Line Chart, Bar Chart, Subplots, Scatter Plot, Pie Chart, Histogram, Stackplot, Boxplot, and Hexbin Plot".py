import matplotlib.pyplot as plt
import numpy as np

# Line Chart
x = np.linspace(0, 10, 100)
y = np.sin(x) 
plt.figure()
plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 25]
plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Subplots
plt.figure()
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y)

# Scatter Plot
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)
plt.figure()
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Pie Chart
sizes = [300, 221, 215, 125, 110]
labels = ['A', 'B', 'C', 'D', 'E']
plt.figure()
plt.pie(sizes, labels=labels)
plt.title("Pie Chart")

# Histogram
x = np.random.normal(170, 10, 250)
plt.figure()
plt.hist(x)
plt.title("Histogram")

# Stackplot
x = [1, 2, 3, 4, 5]
area1 = [2, 3, 2, 5, 4]
area2 = [2, 3, 2, 5, 4]
area3 = [2, 3, 2, 5, 4]
labels = ["area1", "area2", "area3"]
plt.figure()
plt.stackplot(x, area1, area2, area3, labels=labels, colors=["r", "g", "m"], baseline="zero")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc=2)
plt.title("Stackplot")

# Boxplot
data = [np.random.normal(10, 40, 100), np.random.normal(30, 90, 100)]
plt.figure()
plt.boxplot(data)
plt.title('Boxplot')
plt.xlabel('Data Sets')
plt.ylabel('Values')

# Hexbin Plot
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.figure()
plt.hexbin(x, y, gridsize=30, bins='log')
plt.colorbar(label='log10(N)')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Hexbin Plot')

# Show all plots
plt.show()
