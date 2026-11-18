import cv2
import numpy as np

img = cv2.imread('input.jpeg')

if img is None:
    print("Error: Could not load image.")
else:
    # Define a 5x5 structuring element (kernel)
    kernel = np.ones((5, 5), np.uint8)

    # Apply Dilation
    dilated_img = cv2.dilate(img, kernel, iterations=1)

    # Display results
    cv2.imshow('Original', img)
    cv2.imshow('Dilated Image', dilated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
