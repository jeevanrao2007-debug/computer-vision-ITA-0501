"""Experiment 34: draw a circle on a white image."""
import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=600)
    parser.add_argument("--height", type=int, default=400)
    args = parser.parse_args()
    image = np.full((args.height, args.width, 3), 255, dtype=np.uint8)
    radius = min(args.width, args.height) // 4
    cv2.circle(image, (args.width // 2, args.height // 2), radius, (255, 0, 0), 3)
    cv2.imshow("Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()