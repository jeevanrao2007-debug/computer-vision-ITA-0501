"""Experiment 16: Sobel horizontal, vertical, and combined gradients."""
from pathlib import Path
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-display", action="store_true")
    args = parser.parse_args()

    folder = Path(__file__).resolve().parent
    input_path = folder / "INPUT.jpeg"
    if not input_path.exists():
        input_path = folder / "image.jpeg"
    image = cv2.imread(str(input_path))
    if image is None:
        print(f"Error: Could not load {input_path}. Place INPUT.jpeg in the lab folder.")
        return

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradient_x = cv2.Sobel(grayscale, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(grayscale, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x = cv2.convertScaleAbs(gradient_x)
    sobel_y = cv2.convertScaleAbs(gradient_y)
    combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    cv2.imwrite(str(folder / "EXP16_original.jpg"), image)
    cv2.imwrite(str(folder / "sobel_x.jpg"), sobel_x)
    cv2.imwrite(str(folder / "sobel_y.jpg"), sobel_y)
    cv2.imwrite(str(folder / "sobel_combined.jpg"), combined)
    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("Sobel X - Horizontal Gradient", sobel_x)
        cv2.imshow("Sobel Y - Vertical Gradient", sobel_y)
        cv2.imshow("Combined Sobel Gradient", combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()