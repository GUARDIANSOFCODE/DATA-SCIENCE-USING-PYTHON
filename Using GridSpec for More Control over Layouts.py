import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 2, figure=fig)

# First Plot
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot([1, 2, 3], [1, 4, 9], label="Plot 1")
ax1.legend()
ax1.set_title("Plot 1")

# Second Plot
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(["A", "B", "C"], [5, 7, 3], color="orange", label="Plot 2")
ax2.legend()
ax2.set_title("Plot 2")

# Third Plot
ax3 = fig.add_subplot(gs[1, 0])
ax3.scatter([1, 2, 3], [3, 5, 7], color="green", label="Plot 3")
ax3.legend()
ax3.set_title("Plot 3")

# Fourth Plot
ax4 = fig.add_subplot(gs[1, 1])
ax4.hist([1, 2, 1, 3, 2, 1], bins=3, color="purple", label="Plot 4")
ax4.legend()
ax4.set_title("Plot 4")

plt.tight_layout()
plt.show()
