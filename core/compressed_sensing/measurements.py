"""
Module for taking compressed measurements of signals.
"""
import numpy as np

def take_measurements(phi, x, noise_std=0.0):
    """Computes y = Phi * x + noise."""
    y = np.dot(phi, x)
    if noise_std > 0:
        y += np.random.randn(*y.shape) * noise_std
    return y
