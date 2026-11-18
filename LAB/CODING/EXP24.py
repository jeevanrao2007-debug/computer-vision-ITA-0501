"""Experiment 24: black-hat morphological operation."""
from pathlib import Path
import cv2
import numpy as np


def main():
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, np.ones((15, 15), np.uint8))
    cv2.imshow("Original Grayscale", gray)
    cv2.imshow("Black Hat", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()