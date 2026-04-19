"""
Module for generating various types of sensing matrices for compressed sensing.
"""
import numpy as np

def generate_gaussian_matrix(m, n, seed=None):
    """Generates a Gaussian random measurement matrix."""
    rng = np.random.default_rng(seed)
    return rng.standard_normal((m, n)) / np.sqrt(m)

def generate_bernoulli_matrix(m, n, seed=None):
    """Generates a Bernoulli random measurement matrix."""
    rng = np.random.default_rng(seed)
    return (rng.integers(0, 2, (m, n)) * 2 - 1) / np.sqrt(m)
