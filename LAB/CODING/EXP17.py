"""Experiment 17: visible text watermarking."""
from pathlib import Path
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-display", action="store_true")
    parser.add_argument("--text", default="Image Processing Lab")
    args = parser.parse_args()

    folder = Path(__file__).resolve().parent
    input_path = folder / "INPUT.jpeg"
    if not input_path.exists():
        input_path = folder / "image.jpeg"
    original = cv2.imread(str(input_path))
    if original is None:
        print(f"Error: Could not load {input_path}. Place INPUT.jpeg in the lab folder.")
        return

    watermarked = original.copy()
    height, width = watermarked.shape[:2]
    position = (max(10, width // 40), max(30, height - height // 20))
    scale = max(0.5, min(1.5, width / 900))
    # This is visible text watermarking; the original image is unchanged.
    cv2.putText(watermarked, args.text, position, cv2.FONT_HERSHEY_SIMPLEX,
                scale, (0, 0, 0), 4, cv2.LINE_AA)
    cv2.putText(watermarked, args.text, position, cv2.FONT_HERSHEY_SIMPLEX,
                scale, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imwrite(str(folder / "EXP17_original.jpg"), original)
    cv2.imwrite(str(folder / "watermarked.jpg"), watermarked)
    if not args.no_display:
        cv2.imshow("Original Image", original)
        cv2.imshow("Watermarked Image", watermarked)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()