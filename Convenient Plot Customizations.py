import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, label='Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')
plt.legend()
plt.grid(True)
plt.show()
