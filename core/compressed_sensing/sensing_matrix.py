"""
Module for generating various types of sensing matrices for compressed sensing.
"""
import numpy as np

def generate_gaussian_matrix(m, n):
    """Generates a Gaussian random measurement matrix."""
    return np.random.randn(m, n) / np.sqrt(m)

def generate_bernoulli_matrix(m, n):
    """Generates a Bernoulli random measurement matrix."""
    return (np.random.randint(0, 2, (m, n)) * 2 - 1) / np.sqrt(m)
