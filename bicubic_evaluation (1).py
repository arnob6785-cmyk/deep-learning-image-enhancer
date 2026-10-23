
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

# Dataset paths
base_path = "/content/sample_dataset_ready/sample_dataset"
original_dir = os.path.join(base_path, "Original Image")
lr_dir = os.path.join(base_path, "Low Resolution Image")

# Check dataset folders
if not os.path.isdir(original_dir) or not os.path.isdir(lr_dir):
    raise FileNotFoundError("Please check the dataset folder paths.")

extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

original_files = sorted([
    f for f in os.listdir(original_dir)
    if f.lower().endswith(extensions)
])

lr_files = sorted([
    f for f in os.listdir(lr_dir)
    if f.lower().endswith(extensions)
])

lr_lookup = {f.lower(): f for f in lr_files}

results = []
comparison_images = []

# Evaluate each matching image pair
for filename in original_files:

    if filename.lower() not in lr_lookup:
        print("Matching image not found:", filename)
        continue

    original_path = os.path.join(original_dir, filename)
    lr_path = os.path.join(lr_dir, lr_lookup[filename.lower()])

    with Image.open(original_path) as img:
        original = img.convert("RGB")

    with Image.open(lr_path) as img:
        low_res = img.convert("RGB")

    # Bicubic reconstruction
    bicubic = low_res.resize(
        original.size, Image.Resampling.BICUBIC
    )

    original_array = np.array(original)
    bicubic_array = np.array(bicubic)

    # Calculate PSNR
    psnr = peak_signal_noise_ratio(
        original_array,
        bicubic_array,
        data_range=255
    )

    # Calculate SSIM
    ssim = structural_similarity(
        original_array,
        bicubic_array,
        channel_axis=2,
        data_range=255
    )

    results.append({
        "Image": filename,
        "PSNR (dB)": round(float(psnr), 4),
        "SSIM": round(float(ssim), 4)
    })

    comparison_images.append(
        (filename, original.copy(), low_res.copy(), bicubic.copy())
    )

# Stop if no matching image pairs were found
if not results:
    raise ValueError("No matching original and low-resolution image pairs found.")

# Display evaluation results
df = pd.DataFrame(results)

print("BICUBIC EVALUATION RESULTS")
print(df.to_string(index=False))

print("\nAverage PSNR:",
      round(df["PSNR (dB)"].mean(), 4), "dB")

print("Average SSIM:",
      round(df["SSIM"].mean(), 4))

print("Total evaluated image pairs:", len(df))

# Save CSV results
csv_path = "bicubic_evaluation_results.csv"
df.to_csv(csv_path, index=False)

print("\nResults saved to:", csv_path)

# Display Original, Low-Resolution, and Bicubic images
for filename, original, low_res, bicubic in comparison_images:

    fig, axes = plt.subplots(1, 3, figsize=(13, 4))

    axes[0].imshow(original)
    axes[0].set_title("Original Image")

    # Enlarge LR image only for visualization
    enlarged_lr = low_res.resize(
        original.size, Image.Resampling.NEAREST
    )
    axes[1].imshow(enlarged_lr)
    axes[1].set_title("Low-Resolution (Enlarged)")

    axes[2].imshow(bicubic)
    axes[2].set_title("Bicubic Reconstruction")

    for ax in axes:
        ax.axis("off")

    plt.suptitle(filename)
    plt.tight_layout()
    plt.show()
