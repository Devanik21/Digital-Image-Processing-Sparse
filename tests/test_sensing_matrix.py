"""
Tests for sensing matrix generation.
"""
import unittest
import numpy as np
from core.compressed_sensing.sensing_matrix import generate_gaussian_matrix

class TestSensingMatrix(unittest.TestCase):
    def test_gaussian_shape(self):
        mat = generate_gaussian_matrix(50, 100)
        self.assertEqual(mat.shape, (50, 100))

if __name__ == '__main__':
    unittest.main()
