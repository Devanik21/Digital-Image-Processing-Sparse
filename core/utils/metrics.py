"""
Evaluation metrics for image and signal recovery.
"""
import numpy as np

def compute_psnr(img1, img2):
    """Computes Peak Signal-to-Noise Ratio."""
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    return 20 * np.log10(255.0 / np.sqrt(mse))
