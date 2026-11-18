import cv2

# 1. Read the input image
img = cv2.imread('image.jpeg')

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    # 2. Apply Canny Edge Detector
    # 100 is the lower threshold, 200 is the upper threshold
    edges = cv2.Canny(img, 100, 200)

    # 3. Save and display the results
    cv2.imwrite('outline_output.jpg', edges)
    cv2.imshow('Original Image', img)
    cv2.imshow('Outline (Canny Edges)', edges)

    # 4. Keep windows open until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
