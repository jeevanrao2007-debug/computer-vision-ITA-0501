"""Experiment 28: vehicle detection in video using motion contours."""
from pathlib import Path
import cv2


def main():
    path = Path(__file__).resolve().parent / "video.mp4"
    capture = cv2.VideoCapture(str(path))
    background = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        mask = background.apply(frame)
        mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, None, iterations=2)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, width, height = cv2.boundingRect(contour)
            if width * height < 1500 or width < 30 or height < 20:
                continue
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 255), 2)
            cv2.putText(frame, "Vehicle candidate", (x, max(20, y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()