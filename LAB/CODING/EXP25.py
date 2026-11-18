"""Experiment 25: simple general watch-object recognition using shape features."""
from pathlib import Path
import cv2


def main():
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    result = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 40, param1=100, param2=45, minRadius=15, maxRadius=250)
    if circles is not None:
        for x, y, radius in circles[0].astype(int):
            cv2.circle(result, (x, y), radius, (0, 255, 0), 2)
            cv2.putText(result, "Watch candidate", (x - radius, max(25, y - radius - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(result, "No watch candidate detected", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow("Watch Recognition", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()