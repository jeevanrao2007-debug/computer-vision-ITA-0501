"""Experiment 31: threshold-based image segmentation."""
from pathlib import Path
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=127)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, segmented = cv2.threshold(gray, args.threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow("Original Image", image)
    cv2.imshow("Threshold Segmentation", segmented)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()