# Digital Image Processing Sparse

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square) ![Stars](https://img.shields.io/github/stars/Devanik21/Digital-Image-Processing-Sparse?style=flat-square&color=yellow) ![Forks](https://img.shields.io/github/forks/Devanik21/Digital-Image-Processing-Sparse?style=flat-square&color=blue) ![Author](https://img.shields.io/badge/Author-Devanik21-black?style=flat-square&logo=github) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> Sparse representations in digital image processing — compressed sensing, dictionary learning, and sparsity-promoting signal recovery.

---

**Topics:** `computer-vision` · `digital-image-processing` · `dsp-algorithms` · `educational-tools` · `image-denoising` · `image-processing-techniques` · `object-detection` · `streamlit-app`

## Overview

This project explores sparse representation theory in the context of digital image processing —
one of the most mathematically elegant and practically powerful ideas in modern signal processing.
Sparse representations model natural images as a linear combination of a small number of atoms
from an overcomplete dictionary, enabling dramatic compression, robust noise removal, and
separation of signal from corruption using convex optimisation.

The theoretical foundation is Compressed Sensing (Candès, Romberg, Tao; Donoho 2006): a sparse
signal can be recovered from far fewer measurements than the Nyquist rate suggests, provided the
measurement matrix satisfies the Restricted Isometry Property (RIP). The practical implication
is profound — images can be acquired at 20–30% of their pixel count and exactly recovered.
This project implements the full CS pipeline: random measurement, sparse recovery via LASSO,
Orthogonal Matching Pursuit (OMP), and ISTA/FISTA, with visual demonstration of recovery quality
versus measurement rate.

Beyond compressed sensing, the project implements Dictionary Learning (K-SVD algorithm) — learning
an overcomplete dictionary optimally adapted to a training set of image patches. The learned
dictionary, unlike fixed bases (DCT, wavelet), captures the statistical structure of the specific
image class (faces, textures, medical images) and produces sparser representations with lower
reconstruction error.

---

## Motivation

Sparse representations bridge pure mathematics (convex optimisation, measure theory, random matrix
theory) and practical engineering (medical imaging acceleration, satellite image compression,
hyperspectral unmixing). This project was built to make those bridges concrete and computational —
to show that the elegance of l1-minimisation and the RIP condition translate directly into
visible image quality improvements in working code.

---

## Architecture

```
Image or Signal Input
        │
  ┌──────────────────────────────────────────────┐
  │  Compressed Sensing Pipeline:               │
  │  ├── Random measurement matrix Φ (m × n)   │
  │  ├── Measurements y = Φx + noise           │
  │  └── Sparse recovery: min ||x||₁ s.t. Φx≈y │
  │      (LASSO / OMP / ISTA / FISTA)           │
  └──────────────────────────────────────────────┘
        │
  ┌──────────────────────────────────────────────┐
  │  Dictionary Learning (K-SVD):               │
  │  min_{D,X} ||Y - DX||_F  s.t. ||xᵢ||₀ ≤ T │
  │  ├── Sparse coding: OMP per patch           │
  │  └── Dictionary update: SVD per atom        │
  └──────────────────────────────────────────────┘
        │
  PSNR/SSIM evaluation vs. original image
```

---

## Features

### Compressed Sensing Simulation
Full CS pipeline: generate Gaussian random measurement matrices, compute underdetermined measurements, and recover the original signal via L1-minimisation at configurable measurement ratios (10%–80%).

### Sparse Recovery Algorithms
Implementation and comparison of four sparse recovery methods: LASSO (sklearn), Orthogonal Matching Pursuit (OMP), Iterative Shrinkage Thresholding (ISTA), and Fast ISTA (FISTA) — with convergence curves and recovery quality comparison.

### K-SVD Dictionary Learning
Full K-SVD algorithm implementation: initialise dictionary with random patches, iterate between OMP sparse coding and SVD-based atom update until convergence — learning a data-adaptive overcomplete dictionary.

### Fixed Basis Comparison
Sparse representation comparison across DCT basis, Haar wavelet, Daubechies-4 wavelet, and K-SVD learned dictionary — demonstrating the superiority of learned dictionaries for domain-specific images.

### Image Denoising via Sparse Coding
Patch-based image denoising using the sparse coding approach: extract overlapping patches, find sparse representation over the dictionary, reconstruct denoised image via weighted averaging of decoded patches.

### Inpainting via Sparse Recovery
Fill missing or corrupted image regions by treating missing pixels as unmeasured entries in a CS problem and recovering the full image via L1-constrained recovery.

### RIP Condition Visualisation
Empirical verification of the Restricted Isometry Property for random Gaussian, Bernoulli, and structured measurement matrices — visualising the singular value distribution of sub-matrices.

### Recovery Phase Transition Plot
Phase transition diagram: probability of exact sparse recovery as a function of sparsity level and measurement ratio — reproducing the fundamental theoretical result of Donoho and Tanner empirically.

---

## Tech Stack

| Library / Tool | Role | Why This Choice |
|---|---|---|
| **NumPy / SciPy** | Core linear algebra | L1-minimisation, SVD, random matrix generation, OMP |
| **scikit-learn** | LASSO solver | Lasso, OrthogonalMatchingPursuit, sparse solvers |
| **PyWavelets** | Wavelet basis | Haar, Daubechies, biorthogonal wavelet dictionaries |
| **OpenCV / Pillow** | Image I/O | Image loading, patch extraction, reconstruction |
| **scikit-image** | Quality metrics | PSNR, SSIM evaluation |
| **Matplotlib / Plotly** | Visualisation | Dictionary atoms, phase transitions, recovery quality |
| **cvxpy (optional)** | Convex optimisation | L1-minimisation via disciplined convex programming |

---

## Getting Started

### Prerequisites

- Python 3.9+ (or Node.js 18+ for TypeScript/JavaScript projects)
- A virtual environment manager (`venv`, `conda`, or equivalent)
- API keys as listed in the Configuration section

### Installation

```bash
git clone https://github.com/Devanik21/Digital-Image-Processing-Sparse.git
cd Digital-Image-Processing-Sparse
python -m venv venv && source venv/bin/activate
pip install numpy scipy scikit-learn pywavelets opencv-python scikit-image matplotlib plotly
pip install cvxpy  # optional, for exact L1 via convex programming
pip install streamlit  # for interactive demo
streamlit run app.py
```

---

## Usage

```bash
# Compressed sensing recovery demo
python compressed_sensing.py --image lena.png --measurement_ratio 0.3 --recovery omp

# K-SVD dictionary learning
python ksvd.py --train_images training_patches/ --dict_size 256 --sparsity 5

# Image denoising via sparse coding
python sparse_denoise.py --image noisy.png --dictionary dict_ksvd.npy --sparsity 5

# Phase transition experiment
python phase_transition.py --n_trials 1000 --max_sparsity 50 --n_measurements 100
```

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `DICT_SIZE` | `256` | Number of atoms in the learned dictionary |
| `PATCH_SIZE` | `8` | Image patch size in pixels (8×8 default) |
| `SPARSITY_LEVEL` | `5` | Maximum non-zeros per sparse code (T₀) |
| `MEASUREMENT_RATIO` | `0.3` | CS measurement ratio m/n (0.1 to 1.0) |
| `RECOVERY_METHOD` | `omp` | Sparse recovery: omp, lasso, ista, fista, cvxpy |

> Copy `.env.example` to `.env` and populate required values before running.

---

## Project Structure

```
Digital-Image-Processing-Sparse/
├── README.md
├── requirements.txt
├── DIP.py
└── ...
```

---

## Roadmap

- [ ] Total Variation (TV) regularisation as an alternative to l1 for piecewise-constant images
- [ ] Deep unrolling: implement ISTA as a trainable neural network (LISTA) for learned sparse recovery
- [ ] Hyperspectral unmixing: extend sparse coding to multiband image endmember extraction
- [ ] Seismic trace reconstruction: apply CS to seismic acquisition gap filling
- [ ] Distributed CS: sketch-and-solve approach for distributed signal acquisition

---

## Contributing

Contributions, issues, and suggestions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-idea`
3. Commit your changes: `git commit -m 'feat: add your idea'`
4. Push to your branch: `git push origin feature/your-idea`
5. Open a Pull Request with a clear description

Please follow conventional commit messages and add documentation for new features.

---

## Notes

K-SVD dictionary learning is computationally intensive — training on 50,000 patches of size 8×8 takes approximately 5–15 minutes per 10 iterations of K-SVD. Use a smaller patch database or reduce iterations for faster experimentation. CVXPY-based exact L1 minimisation is much slower than iterative algorithms (ISTA/FISTA) but provides exact results for verification.

---

## Author

**Devanik Debnath**  
B.Tech, Electronics & Communication Engineering  
National Institute of Technology Agartala

[![GitHub](https://img.shields.io/badge/GitHub-Devanik21-black?style=flat-square&logo=github)](https://github.com/Devanik21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devanik-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/devanik/)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with curiosity, depth, and care — because good projects deserve good documentation.*
