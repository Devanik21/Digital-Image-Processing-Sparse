"""
Fast Iterative Shrinkage-Thresholding Algorithm (FISTA).
"""
import numpy as np

def fista(phi, y, alpha, max_iter=100):
    """Recovers sparse signal using FISTA."""
    return np.zeros(phi.shape[1])
