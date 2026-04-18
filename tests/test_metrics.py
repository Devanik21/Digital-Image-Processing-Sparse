"""
Tests for evaluation metrics.
"""
import unittest
import numpy as np
from core.utils.metrics import compute_psnr

class TestMetrics(unittest.TestCase):
    def test_psnr_identical(self):
        img = np.ones((10, 10)) * 128
        psnr = compute_psnr(img, img)
        self.assertTrue(np.isinf(psnr))

if __name__ == '__main__':
    unittest.main()
