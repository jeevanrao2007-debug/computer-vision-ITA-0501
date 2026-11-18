"""Experiment 40: extract and display text detected in video frames."""
from pathlib import Path
import argparse
import cv2
import os
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", default="eng")
    parser.add_argument(
        "--tesseract-cmd",
        default=os.environ.get("TESSERACT_CMD"),
        help="path to the Tesseract executable (or set TESSERACT_CMD)",
    )
    args = parser.parse_args()
    try:
        import pytesseract
    except ImportError:
        print("Install the optional OCR package first: pip install pytesseract")
        return
    tesseract_cmd = (
        str(Path(args.tesseract_cmd).resolve())
        if args.tesseract_cmd and Path(args.tesseract_cmd).is_file()
        else shutil.which(args.tesseract_cmd or "tesseract")
    )
    if not tesseract_cmd:
        print(
            "Error: Tesseract OCR is not installed or is not on PATH. "
            "Install Tesseract, then run again, or use "
            "--tesseract-cmd <path-to-tesseract.exe>."
        )
        return
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    path = Path(__file__).resolve().parent / "video.mp4"
    capture = cv2.VideoCapture(str(path))
    if not capture.isOpened():
        print(f"Error: Could not open {path}.")
        return
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        text = pytesseract.image_to_string(frame, lang=args.language).strip()
        display = frame.copy()
        cv2.putText(display, text[:80] or "No text detected", (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Video Text Extraction", display)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()