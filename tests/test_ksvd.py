"""
Tests for K-SVD Dictionary Learning.
"""
import unittest
from core.dictionary_learning.ksvd import KSVD

class TestKSVD(unittest.TestCase):
    def test_init(self):
        model = KSVD(n_components=128)
        self.assertEqual(model.n_components, 128)

if __name__ == '__main__':
    unittest.main()
