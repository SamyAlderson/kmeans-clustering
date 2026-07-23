import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_clustering(data, k):
    """
    Perform K-means clustering on the given data.

    Args:
    data (numpy.array): Input data points.
    k (int): Number of clusters.

    Returns:
    centers (numpy.array): Coordinates of the cluster centers.
    labels (numpy.array): Labels of the data points corresponding to their assigned clusters.
    """
    # K-means clustering using scikit-learn
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    
    # Get the cluster centers and labels
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    return centers, labels


def initialize_clusters(data, k):
    """
    Initialize the cluster centers randomly from the input data.

    Args:
    data (numpy.array): Input data points.
    k (int): Number of clusters.

    Returns:
    init_centers (numpy.array): Randomly initialized cluster centers.
    """
    # Initialize the cluster centers randomly from the input data
    init_centers = np.random.choice(data, size=k, replace=False)
    
    return init_centers


def update_clusters(data, centers):
    """
    Update the cluster centers based on the current cluster assignments.

    Args:
    data (numpy.array): Input data points.
    centers (numpy.array): Current cluster centers.

    Returns:
    new_centers (numpy.array): Updated cluster centers.
    """
    # Update the cluster centers by taking the mean of all data points assigned to each cluster
    new_centers = np.array([data[kmeans.labels_ == i].mean(axis=0) for i in range(k)])
    
    return new_centers


def kmeans(data, k, max_iter=100):
    """
    Perform K-means clustering on the given data.

    Args:
    data (numpy.array): Input data points.
    k (int): Number of clusters.
    max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
    centers (numpy.array): Coordinates of the cluster centers.
    labels (numpy.array): Labels of the data points corresponding to their assigned clusters.
    """
    # Initialize the cluster centers randomly
    centers = initialize_clusters(data, k)
    
    for _ in range(max_iter):
        # Assign each data point to the closest cluster
        closest_centers = np.argmin(np.linalg.norm(data[:, np.newaxis] - centers, axis=2), axis=1)
        
        # Update the cluster centers
        centers = update_clusters(data, centers)
        
        # Check for convergence
        if np.all(closest_centers == kmeans_clustering(data, k)[1]):
            break
    
    # Get the final cluster centers and labels
    centers, labels = kmeans_clustering(data, k)
    
    return centers, labels


# Example usage:
if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.multivariate_normal([0, 0], [[1, 0.75], [0.75, 1]], 100)
    k = 3
    centers, labels = kmeans(data, k)
    
    # Visualize the clusters
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.scatter(centers[:, 0], centers[:, 1], c='red')
    plt.show()