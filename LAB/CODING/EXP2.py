import cv2

img = cv2.imread('input.jpeg')

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(img, (5, 5), 9)

    # Save and display
    cv2.imwrite('blurred_output.jpg', blurred)
    cv2.imshow('Blurred Output', blurred)
    cv2.imshow('Input Image', img)  # Fixed: changed 'image' to 'img'

    cv2.waitKey(0)
    cv2.destroyAllWindows()
