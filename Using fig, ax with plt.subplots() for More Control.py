import matplotlib.pyplot as plt

# Create a figure with two subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# First Plot on ax1
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [300, 350, 200, 400, 450]
ax1.bar(months, sales, color="green", label="Monthly Sales")
ax1.set_xlabel("Months")
ax1.set_ylabel("Sales")
ax1.legend()
ax1.set_title("Bar Chart - Monthly Sales")

# Second Plot on ax2
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [22, 21, 23, 24, 22, 25, 26]
ax2.plot(day, temp, color="blue", label="Daily Temperature")
ax2.set_xlabel("Days")
ax2.set_ylabel("Temperature (°C)")
ax2.legend()
ax2.set_title("Line Chart - Daily Temperature")

# Adjust layout and display
plt.tight_layout()
plt.show()
