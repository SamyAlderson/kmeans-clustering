import unittest
import numpy as np
from src.kmeans import KMeans

class TestKMeans(unittest.TestCase):

    def test_init(self):
        # Test that KMeans object is created with valid parameters
        kmeans = KMeans(n_clusters=3)
        self.assertEqual(kmeans.n_clusters, 3)

    def test_fit(self):
        # Test that KMeans fit method doesn't throw an error
        np.random.seed(0)
        data = np.random.rand(10, 2)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(data)

    def test_predict(self):
        # Test that KMeans predict method doesn't throw an error
        np.random.seed(0)
        data = np.random.rand(10, 2)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(data)
        labels = kmeans.predict(data)
        self.assertEqual(labels.shape, data.shape)

    def test_invalid_n_clusters(self):
        # Test that KMeans object raises an error with invalid n_clusters
        with self.assertRaises(ValueError):
            KMeans(n_clusters=-1)

    def test_invalid_data_type(self):
        # Test that KMeans object raises an error with invalid data type
        with self.assertRaises(TypeError):
            KMeans(n_clusters=3)
            KMeans.fit('invalid_data')

if __name__ == '__main__':
    unittest.main()