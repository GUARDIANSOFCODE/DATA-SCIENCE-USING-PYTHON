import matplotlib.pyplot as plt

# Temperature data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperature = [22, 21, 23, 24, 22, 25, 26]

# Creating the line plot
plt.figure(figsize=(10, 5))
plt.plot(days, temperature, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Temperature Change Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
