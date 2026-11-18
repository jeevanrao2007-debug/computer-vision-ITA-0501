"""Experiment 32: white image with four colored corner boxes."""
import argparse
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    args = parser.parse_args()
    width = args.width or int(input("Enter image width: "))
    height = args.height or int(input("Enter image height: "))
    image = np.full((height, width, 3), 255, dtype=np.uint8)
    box_width, box_height = max(1, width // 10), max(1, height // 10)
    image[:box_height, :box_width] = (0, 0, 0)
    image[:box_height, -box_width:] = (255, 0, 0)
    image[-box_height:, :box_width] = (0, 255, 0)
    image[-box_height:, -box_width:] = (0, 0, 255)
    cv2.imshow("Four Corner Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()