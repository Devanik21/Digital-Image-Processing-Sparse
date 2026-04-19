"""
Initialization methods for dictionary learning.
"""
import numpy as np

def init_random_patches(X, n_components):
    """Initialize dictionary by randomly selecting patches from X."""
    indices = np.random.choice(X.shape[1], n_components, replace=False)
    D = X[:, indices]
    norms = np.linalg.norm(D, axis=0)
    D = D / np.where(norms == 0, 1, norms)
    return D
