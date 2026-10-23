Image Super-Resolution Using a Deep Learning-Based Model

Course:CSE 445 — Machine Learning  
Group: 04  

Project Overview
This project focuses on Single Image Super-Resolution (SISR) to reconstruct high-resolution images from degraded, low-resolution inputs[cite: 4, 5]. We benchmark classical Bicubic Interpolation against a deep learning-based Super-Resolution Convolutional Neural Network (SRCNN)[cite: 4, 5].

Work Division & Current Status
| Member | Role | Contribution (Update 1) |

| Member 1 (Meheraj) | Dataset & Preprocessing | Collected 100 images, created downsampling script, uploaded `Dataset_1.zip` |
| Member 2 | (Mariam) | Model Architecture | Designed 3-layer SRCNN architecture (In progress) |
| Member 3 (Nusrat) | Evaluation & Benchmark | Built `bicubic_evaluation.py`, computed baseline PSNR/SSIM|
| Member 4 (Arnob) | Integration & Documentation | Repository organization, requirements, reports, and presentation |

 Preliminary Baseline Results (Bicubic Interpolation)
Evaluated across sample pairs by Member 3 using `bicubic_evaluation.py`:

| Metric | Baseline Result | Sample Size |

| PSNR | 22.0131 dB | 5 image pairs[cite: 5] |
| SSIM | 0.4788 | 5 image pairs[cite: 5] |

*Note: These baseline metrics represent the structural loss of classical interpolation that our SRCNN deep learning model aims to surpass.
