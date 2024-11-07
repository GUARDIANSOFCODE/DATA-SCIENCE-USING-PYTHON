import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

# First Plot (1 row, 2 columns, position 1)
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9], label="Plot 1")
plt.legend()
plt.title("Plot 1")

# Second Plot (2 rows, 2 columns, position 2)
plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C"], [5, 7, 3], color="orange", label="Plot 2")
plt.legend()
plt.title("Plot 2")

# Third Plot (2 rows, 2 columns, position 3)
plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3], [3, 5, 7], color="green", label="Plot 3")
plt.legend()
plt.title("Plot 3")

# Fourth Plot (2 rows, 2 columns, position 4)
plt.subplot(2, 2, 4)
plt.hist([1, 2, 1, 3, 2, 1], bins=3, color="purple", label="Plot 4")
plt.legend()
plt.title("Plot 4")

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
