import matplotlib.pyplot as plt

# First Plot
plt.figure(1)  # Creates a new figure with ID 1
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [300, 350, 200, 400, 450]
plt.bar(months, sales, color="green", label="Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.title("Bar Chart - Monthly Sales")

# Second Plot
plt.figure(2)  # Creates a new figure with ID 2
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [22, 21, 23, 24, 22, 25, 26]
plt.plot(day, temp, color="blue", label="Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title("Line Chart - Daily Temperature")

# Show all plots
plt.show()
