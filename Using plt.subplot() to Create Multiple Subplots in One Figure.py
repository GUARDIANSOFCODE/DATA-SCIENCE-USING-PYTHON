import matplotlib.pyplot as plt

# Define the overall figure
plt.figure(figsize=(10, 5))  # Set the size of the figure

# First Plot - Top Left (1 row, 2 columns, 1st position)
plt.subplot(1, 2, 1)
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [300, 350, 200, 400, 450]
plt.bar(months, sales, color="green", label="Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.title("Bar Chart - Monthly Sales")

# Second Plot - Top Right (1 row, 2 columns, 2nd position)
plt.subplot(1, 2, 2)
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [22, 21, 23, 24, 22, 25, 26]
plt.plot(day, temp, color="blue", label="Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title("Line Chart - Daily Temperature")

# Show both subplots in the same figure
plt.tight_layout()  # Adjust spacing between plots for better readability
plt.show()
