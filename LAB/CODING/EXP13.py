"""Experiment 13: affine transformation using three point pairs."""
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

    height, width = image.shape[:2]
    source_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
    destination_points = np.float32([
        [int(width * 0.10), int(height * 0.10)],
        [int(width * 0.90), int(height * 0.05)],
        [int(width * 0.05), int(height * 0.90)],
    ])
    matrix = cv2.getAffineTransform(source_points, destination_points)
    transformed = cv2.warpAffine(image, matrix, (width, height))
    cv2.imwrite(str(folder / "EXP13_original.jpg"), image)
    cv2.imwrite(str(folder / "affine_transformation.jpg"), transformed)
    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("Affine Transformation", transformed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()