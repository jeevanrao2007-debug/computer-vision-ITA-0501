import cv2
import numpy as np

# 1. Read the input image
img = cv2.imread('input.jpeg')

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    # 2. Define a 5x5 kernel (structuring element) of ones
    kernel = np.ones((5, 5), np.uint8)

    # 3. Apply the erosion operation
    eroded_img = cv2.erode(img, kernel, iterations=1)

    # 4. Save and display the results
    cv2.imwrite('eroded_output.jpg', eroded_img)
    cv2.imshow('Original Image', img)
    cv2.imshow('Eroded Image', eroded_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
