# src/main.py

import numpy as np
from sklearn.cluster import KMeans
from src.kmeans import KMeansClustering
from src.utils import load_data

def main():
    # Load sample dataset
    try:
        data = load_data("iris.csv")
    except FileNotFoundError:
        print("Error: Could not find the iris dataset.")
        return

    # Perform K-means clustering
    kmeans = KMeansClustering(n_clusters=3)
    clusters = kmeans.fit(data)

    # Visualize the results
    import matplotlib.pyplot as plt
    plt.scatter(data[:, 0], data[:, 1], c=clusters)
    plt.show()

if __name__ == "__main__":
    main()
```

```python
# src/utils.py

import pandas as pd

def load_data(file_path):
    try:
        return pd.read_csv(file_path).values
    except pd.errors.EmptyDataError:
        print("Error: The dataset is empty.")
        raise
```

```python
# src/kmeans.py

import numpy as np

class KMeansClustering:
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters

    def fit(self, data):
        # Initialize centroids randomly
        centroids = data[np.random.choice(data.shape[0], size=self.n_clusters, replace=False)]

        while True:
            # Assign each point to the closest centroid
            distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
            closest_centroids = np.argmin(distances, axis=1)

            # Update centroids as the mean of points in each cluster
            new_centroids = np.array([data[closest_centroids == i].mean(axis=0) for i in range(self.n_clusters)])

            # Check for convergence
            if np.all(centroids == new_centroids):
                break

            centroids = new_centroids

        return closest_centroids
```

```python
# tests/test_kmeans.py

import unittest
import numpy as np
from src.kmeans import KMeansClustering

class TestKMeans(unittest.TestCase):
    def test_kmeans(self):
        data = np.random.rand(100, 2)
        kmeans = KMeansClustering(n_clusters=3)
        clusters = kmeans.fit(data)
        self.assertEqual(clusters.shape, (100,))

if __name__ == "__main__":
    unittest.main()