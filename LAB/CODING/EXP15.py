"""Experiment 15: Harris corner detection."""
from pathlib import Path
import argparse
import cv2
import numpy as np


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

    grayscale = np.float32(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    response = cv2.cornerHarris(grayscale, 2, 3, 0.04)
    response = cv2.dilate(response, None)
    result = image.copy()
    threshold = 0.01 * response.max()
    result[response > threshold] = [0, 0, 255]
    cv2.imwrite(str(folder / "EXP15_original.jpg"), image)
    cv2.imwrite(str(folder / "harris_corners.jpg"), result)
    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("Harris Corner Detection", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()