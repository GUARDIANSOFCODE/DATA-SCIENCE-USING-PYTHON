import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# First Plot
ax[0, 0].plot([1, 2, 3], [1, 4, 9], label="Plot 1")
ax[0, 0].legend()
ax[0, 0].set_title("Plot 1")

# Second Plot
ax[0, 1].bar(["A", "B", "C"], [5, 7, 3], color="orange", label="Plot 2")
ax[0, 1].legend()
ax[0, 1].set_title("Plot 2")

# Third Plot
ax[1, 0].scatter([1, 2, 3], [3, 5, 7], color="green", label="Plot 3")
ax[1, 0].legend()
ax[1, 0].set_title("Plot 3")

# Fourth Plot
ax[1, 1].hist([1, 2, 1, 3, 2, 1], bins=3, color="purple", label="Plot 4")
ax[1, 1].legend()
ax[1, 1].set_title("Plot 4")

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
