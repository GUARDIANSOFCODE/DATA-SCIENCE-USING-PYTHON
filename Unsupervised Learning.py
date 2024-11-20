# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
data = np.array([
    [1, 2], [2, 3], [3, 4], [5, 6],
    [8, 8], [9, 10], [10, 12], [12, 14]
])

# K-Means Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plotting
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x')
plt.title('K-Means Clustering')
plt.show()
