"""Experiment 26: display video frames in reverse order."""
from pathlib import Path
import cv2


def main():
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
        cv2.imshow("Reverse Video", frame)
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()