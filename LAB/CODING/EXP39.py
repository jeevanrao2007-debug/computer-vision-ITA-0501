"""Experiment 39: play video in reverse slow motion."""
from pathlib import Path
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay", type=int, default=120, help="milliseconds between reverse frames")
    args = parser.parse_args()
    path = Path(__file__).resolve().parent / "video.mp4"
    capture = cv2.VideoCapture(str(path))
    frames = []
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        frames.append(frame)
    capture.release()
    if not frames:
        print(f"Error: Could not read {path}.")
        return
    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)
        if cv2.waitKey(max(1, args.delay)) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()