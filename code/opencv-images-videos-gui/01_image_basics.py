"""
Image Basics: Understanding how images are represented in memory.

This script demonstrates:
- Creating images with NumPy arrays
- Grayscale vs BGR color formats
- Image properties: shape, size, dtype
"""

import numpy as np
import cv2

# Create a 3x3 black grayscale image
print("Creating a 3x3 grayscale image (all zeros = black):")
gray_img = np.zeros((3, 3), dtype=np.uint8)
print(gray_img)
print(f"Shape: {gray_img.shape}")
print(f"Size: {gray_img.size}")
print(f"Dtype: {gray_img.dtype}")
print()

# Convert to BGR (color) format
print("Converting to BGR (color) format:")
color_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
print(color_img)
print(f"Shape: {color_img.shape}")
print(f"Size: {color_img.size}")
print()

# Create a larger image with some colors
print("Creating a 100x100 image with colored quadrants:")
img = np.zeros((100, 100, 3), dtype=np.uint8)

# Top-left: Blue (BGR = [255, 0, 0])
img[0:50, 0:50] = [255, 0, 0]

# Top-right: Green (BGR = [0, 255, 0])
img[0:50, 50:100] = [0, 255, 0]

# Bottom-left: Red (BGR = [0, 0, 255])
img[50:100, 0:50] = [0, 0, 255]

# Bottom-right: White (BGR = [255, 255, 255])
img[50:100, 50:100] = [255, 255, 255]

# Save the image to see the result
cv2.imwrite('colored_quadrants.png', img)
print("Saved 'colored_quadrants.png' - open it to see the result!")
print(f"Shape: {img.shape} (height, width, channels)")

# Generate and save the image to see the result
random_img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
cv2.imwrite('random_color.png', random_img)
