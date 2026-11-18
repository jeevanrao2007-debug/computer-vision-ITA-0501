"""Experiment 18: crop, copy, and paste a selected region of interest."""
from pathlib import Path
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=-1)
    parser.add_argument("--y", type=int, default=-1)
    parser.add_argument("--width", type=int, default=200)
    parser.add_argument("--height", type=int, default=150)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    height, width = image.shape[:2]
    x = args.x if args.x >= 0 else width // 4
    y = args.y if args.y >= 0 else height // 4
    x, y = max(0, min(x, width - 1)), max(0, min(y, height - 1))
    roi = image[y:min(y + args.height, height), x:min(x + args.width, width)].copy()
    pasted = image.copy()
    pasted[:roi.shape[0], :roi.shape[1]] = roi
    marked = image.copy()
    cv2.rectangle(marked, (x, y), (x + roi.shape[1], y + roi.shape[0]), (0, 0, 255), 2)
    cv2.imshow("Selected ROI", roi)
    cv2.imshow("Source Image", marked)
    cv2.imshow("Copied ROI Pasted at Top Left", pasted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()