import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    # Load the color image
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Could not load image from '{image_path}'.")
        return

    # Tuple for OpenCV channels and corresponding plot line colors
    colors = ('b', 'g', 'r')
    channel_names = ('Blue Channel', 'Green Channel', 'Red Channel')

    plt.figure(figsize=(10, 5))
    plt.title('Color Histogram Analysis')
    plt.xlabel('Pixel Intensity (0 - 255)')
    plt.ylabel('Pixel Count')

    # Loop through BGR channels
    for i, color in enumerate(colors):
        # cv2.calcHist(images, channels, mask, histSize, ranges)
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=channel_names[i])
        plt.xlim([0, 256])

    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Example Usage
analyze_color_histogram('input.jpeg')
