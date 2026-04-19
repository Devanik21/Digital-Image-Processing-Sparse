"""
Tests for Orthogonal Matching Pursuit.
"""
import unittest
from core.recovery.omp import orthogonal_matching_pursuit
import numpy as np

class TestOMP(unittest.TestCase):
    def test_omp_output_shape(self):
        phi = np.random.randn(50, 100)
        y = np.random.randn(50)
        x = orthogonal_matching_pursuit(phi, y, 5)
        self.assertEqual(x.shape, (100,))

if __name__ == '__main__':
    unittest.main()
