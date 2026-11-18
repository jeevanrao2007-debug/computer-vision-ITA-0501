"""Experiment 36: subtract a selected background color range."""
from pathlib import Path
import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lower", type=int, default=0)
    parser.add_argument("--upper", type=int, default=80)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([0, 0, args.lower]), np.array([180, 255, args.upper]))
    foreground = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    cv2.imshow("Input", image)
    cv2.imshow("Background Removed", foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()