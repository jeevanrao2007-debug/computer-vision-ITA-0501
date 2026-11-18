import cv2
import numpy as np

# 1. Read the image in grayscale
img = cv2.imread('image.jpeg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    # 2. Perform Histogram Equalization
    equalized_img = cv2.equalizeHist(img)

    # 3. Stack original and equalized images side-by-side for comparison
    comparison = np.hstack((img, equalized_img))

    # 4. Save and display results
    cv2.imwrite('equalized_output.jpg', equalized_img)
    cv2.imwrite('comparison_output.jpg', comparison)

    cv2.imshow('Original (Left) vs Equalized (Right)', comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
