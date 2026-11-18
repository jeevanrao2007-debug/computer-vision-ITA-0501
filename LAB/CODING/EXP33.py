"""Experiment 33: draw a rectangle on a white image."""
import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=600)
    parser.add_argument("--height", type=int, default=400)
    args = parser.parse_args()
    image = np.full((args.height, args.width, 3), 255, dtype=np.uint8)
    cv2.rectangle(image, (args.width // 4, args.height // 4), (3 * args.width // 4, 3 * args.height // 4), (0, 0, 255), 3)
    cv2.imshow("Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()