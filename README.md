
# Image Super-Resolution Using a Deep Learning-Based Model

## Project Overview
This project focuses on image super-resolution using deep learning.
The goal is to improve the visual quality and resolution of low-resolution images.

## My Contribution
*Role:* Member 3 - Evaluation and Result Analysis

My responsibilities include:
- Implementing PSNR and SSIM evaluation metrics.
- Evaluating Bicubic interpolation as a baseline method.
- Comparing original, low-resolution, and reconstructed images.
- Analyzing the preliminary evaluation results.

## Evaluation Methodology
Five pairs of original and low-resolution images were used for preliminary evaluation.

The low-resolution images were resized to match the dimensions of their corresponding original images using Bicubic interpolation.

The reconstructed images were evaluated using the following metrics:

- *PSNR (Peak Signal-to-Noise Ratio):* Measures pixel-level reconstruction quality.
- *SSIM (Structural Similarity Index):* Measures structural similarity between the reconstructed and original images.

## Preliminary Results

| Metric | Average Result |
|---|---:|
| PSNR | 22.0131 dB |
| SSIM | 0.4788 |
| Evaluated Image Pairs | 5 |

These results represent the Bicubic baseline evaluation on the sample dataset.

## Files
- bicubic_evaluation.py: Python code for Bicubic reconstruction, PSNR, SSIM, and visual comparison.
- bicubic_evaluation_results.csv: Evaluation results for the sample images.
- README.md: Project contribution and evaluation documentation.

## Future Work
The Bicubic baseline will be compared with the SRCNN model after the model implementation is completed.

SRCNN evaluation results have not yet been included.

## Tools and Libraries
- Python
- NumPy
- Pandas
- Matplotlib
- Pillow
- scikit-image
- Google Colab
