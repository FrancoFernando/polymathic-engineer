"""
Reading and Writing Images: Loading, saving, and manipulating image data.

This script demonstrates:
- Loading images with imread
- Saving images with imwrite
- Modifying individual pixels
- Array slicing for bulk operations
- Copying regions of interest (ROI)
"""

import cv2
import numpy as np


# First, create a sample image to work with
sample_img = np.zeros((200, 200, 3), dtype=np.uint8)
sample_img[:, :] = [100, 150, 200]  # Light brownish color
cv2.imwrite('sample.png', sample_img)
print("Created 'sample.png' as our test image")
print()

# Load an image
img = cv2.imread('sample.png')
print(f"Loaded image shape: {img.shape}")

# Load as grayscale
gray_img = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE)
print(f"Grayscale image shape: {gray_img.shape}")
print()

# Modify a single pixel (top-left corner to white)
img[0, 0] = [255, 255, 255]
print("Set pixel at (0,0) to white")

# Modify a region using array slicing
# Remove all green from the top half
img[0:100, :, 1] = 0
print("Removed green channel from top half")

# Set the bottom-left quadrant to blue
img[100:200, 0:100] = [255, 0, 0]
print("Set bottom-left quadrant to blue")

# Copy a region of interest (ROI)
roi = img[100:150, 100:150]  # 50x50 region from bottom-right area
img[25:75, 25:75] = roi  # Paste it in the top-left area
print("Copied a 50x50 region from bottom-right to top-left")
print()

# Save the modified image
cv2.imwrite('sample_modified.png', img)
print("Saved modified image as 'sample_modified.png'")

# Also save the grayscale version
cv2.imwrite('sample_gray.png', gray_img)
print("Saved grayscale image as 'sample_gray.png'")
