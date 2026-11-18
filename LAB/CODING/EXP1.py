import cv2

# Read the original image
img = cv2.imread(r"C:\Users\Rathi\OneDrive\Desktop\cv\lab\INPUT.jpeg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Original', img)
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

