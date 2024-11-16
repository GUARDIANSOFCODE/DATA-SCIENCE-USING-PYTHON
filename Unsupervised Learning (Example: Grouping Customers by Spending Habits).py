# Importing necessary libraries
from sklearn.cluster import KMeans
import numpy as np

# Customer data: [Annual Income, Spending Score]
data = np.array([
    [15, 39], [16, 81], [17, 6], [18, 77], [19, 40],
    [20, 76], [21, 6], [22, 94], [23, 3], [24, 72]
])

# Applying K-Means clustering to group customers
kmeans = KMeans(n_clusters=2)  # We want 2 groups
kmeans.fit(data)

# Predicting clusters for the data
labels = kmeans.labels_
print("Cluster Labels for Customers:", labels)

# Cluster centers
print("Cluster Centers (Group Representative Points):", kmeans.cluster_centers_)
