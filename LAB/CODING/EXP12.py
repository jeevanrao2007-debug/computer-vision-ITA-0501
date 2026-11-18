"""Experiment 12: 270-degree clockwise image rotation."""
from pathlib import Path
import argparse
import cv2


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

    # The question's y-axis wording is interpreted as standard 2D rotation.
    # 270 degrees clockwise is the same as 90 degrees counterclockwise.
    rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(str(folder / "EXP12_original.jpg"), image)
    cv2.imwrite(str(folder / "rotated_270_clockwise.jpg"), rotated)
    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("270-Degree Clockwise Rotation", rotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()