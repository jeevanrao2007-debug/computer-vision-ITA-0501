"""Experiment 14: perspective transformation using four point pairs."""
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
    margin_x, margin_y = int(width * 0.12), int(height * 0.12)
    source_points = np.float32([
        [margin_x, margin_y], [width - margin_x, margin_y],
        [width - margin_x, height - margin_y], [margin_x, height - margin_y],
    ])
    destination_points = np.float32([
        [0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1],
    ])
    matrix = cv2.getPerspectiveTransform(source_points, destination_points)
    transformed = cv2.warpPerspective(image, matrix, (width, height))
    cv2.imwrite(str(folder / "EXP14_original.jpg"), image)
    cv2.imwrite(str(folder / "perspective_transformation.jpg"), transformed)
    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("Perspective Transformation", transformed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()