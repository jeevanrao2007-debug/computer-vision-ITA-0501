"""Experiment 35: place user-entered text on an image."""
from pathlib import Path
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", default=None)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    text = args.text if args.text is not None else input("Enter text: ")
    cv2.putText(image, text, (30, max(50, image.shape[0] // 2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Text on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()