import cv2

img = cv2.imread('input.jpeg')

if img is None:
    print("Error: Could not load image.")
else:
    height, width = img.shape[:2]

    # 1. Scale down (smaller size - 50% of original)
    smaller_img = cv2.resize(img, (width // 2, height // 2), interpolation=cv2.INTER_AREA)

    # 2. Scale up (bigger size - 200% of original)
    bigger_img = cv2.resize(img, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)

    # Display images
    cv2.imshow('Original', img)
    cv2.imshow('Smaller (50%)', smaller_img)
    cv2.imshow('Bigger (200%)', bigger_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
