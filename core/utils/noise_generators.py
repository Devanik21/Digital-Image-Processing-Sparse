"""
Noise generation utilities for robust testing.
"""
import numpy as np

def add_gaussian_noise(img, sigma):
    """Adds AWGN to an image."""
    return img + np.random.randn(*img.shape) * sigma
