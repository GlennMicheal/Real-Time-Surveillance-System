from sklearn.cluster import KMeans
import numpy as np

# Simulated data representing the frequency of suspicious activity in various zones
data = np.array([[1, 2], [3, 4], [10, 12], [15, 18], [5, 6]])

# Using KMeans clustering to categorize areas based on activity levels
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)

# The algorithm will assign labels to each zone, representing the threat level
labels = kmeans.labels_

for idx, label in enumerate(labels):
    print(f"Zone {idx + 1} is in cluster {label}")
