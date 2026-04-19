"""
Tests for ISTA recovery.
"""
import unittest
from core.recovery.ista import ista
import numpy as np

class TestISTA(unittest.TestCase):
    def test_ista_output_shape(self):
        phi = np.random.randn(50, 100)
        y = np.random.randn(50)
        x = ista(phi, y, 0.1)
        self.assertEqual(x.shape, (100,))

if __name__ == '__main__':
    unittest.main()
