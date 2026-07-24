import unittest
from src.main import kmeans
from src.utils import load_data, save_data

class TestKMeans(unittest.TestCase):
    def test_kmeans(self):
        data = load_data('data.txt')
        centroids = [10.0, 20.0]
        clusters = kmeans(data, centroids)
        save_data(clusters, 'clusters.txt')

if __name__ == '__main__':
    unittest.main()