import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Data for each plot
data = [
    ([1, 2, 3], [1, 4, 9], "Plot 1", "line"),
    (["A", "B", "C"], [5, 7, 3], "Plot 2", "bar"),
    ([1, 2, 3], [3, 5, 7], "Plot 3", "scatter"),
    ([1, 2, 1, 3, 2, 1], None, "Plot 4", "hist")
]

# Create each plot in the loop
for i, (x, y, title, plot_type) in enumerate(data):
    ax = axes[i // 2, i % 2]
    if plot_type == "line":
        ax.plot(x, y, label=title)
    elif plot_type == "bar":
        ax.bar(x, y, label=title)
    elif plot_type == "scatter":
        ax.scatter(x, y, label=title)
    elif plot_type == "hist":
        ax.hist(x, bins=3, label=title)
    ax.legend()
    ax.set_title(title)

plt.tight_layout()
plt.show()
