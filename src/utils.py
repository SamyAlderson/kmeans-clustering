# Import necessary modules
import numpy as np

def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    
    Args:
        point1 (list): The first point.
        point2 (list): The second point.
    
    Returns:
        float: The Euclidean distance between the two points.
    """
    # This was tricky, but numpy's linalg.norm does the job
    return np.linalg.norm(np.array(point1) - np.array(point2))

def calculate_centroid(cluster):
    """
    Calculate the centroid of a cluster.
    
    Args:
        cluster (list): A list of points in the cluster.
    
    Returns:
        list: The centroid of the cluster.
    """
    # Not proud of this but it works
    return np.mean(cluster, axis=0)

def normalize_data(data):
    """
    Normalize the data by subtracting the mean and dividing by the standard deviation.
    
    Args:
        data (numpy array): The data to be normalized.
    
    Returns:
        numpy array: The normalized data.
    """
    # Calculate the mean and standard deviation
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    
    # Check for zero standard deviation
    if np.all(std_dev == 0):
        # If all standard deviations are zero, return the original data
        return data
    
    # Subtract the mean and divide by the standard deviation
    return (data - mean) / std_dev

def check_convergence(centroids, old_centroids):
    """
    Check if the centroids have converged.
    
    Args:
        centroids (list): The current centroids.
        old_centroids (list): The previous centroids.
    
    Returns:
        bool: True if the centroids have converged, False otherwise.
    """
    # Check if the centroids are the same
    return np.array_equal(centroids, old_centroids)

def get_nearest_centroid(point, centroids):
    """
    Get the index of the nearest centroid to a point.
    
    Args:
        point (list): The point.
        centroids (list): The centroids.
    
    Returns:
        int: The index of the nearest centroid.
    """
    # Use numpy's argmin to find the index of the minimum distance
    return np.argmin([calculate_distance(point, centroid) for centroid in centroids])