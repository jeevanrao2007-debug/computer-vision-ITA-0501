"""Experiment 30: smile detection with a Haar cascade."""
from pathlib import Path
import cv2


def main():
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    face = cv2.CascadeClassifier(str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"))
    smile = cv2.CascadeClassifier(str(Path(cv2.data.haarcascades) / "haarcascade_smile.xml"))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    count = 0
    for x, y, width, height in face.detectMultiScale(gray, 1.1, 5):
        region = gray[y:y + height, x:x + width]
        for sx, sy, sw, sh in smile.detectMultiScale(region, 1.7, 20):
            cv2.rectangle(image, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (255, 0, 255), 2)
            count += 1
    cv2.putText(image, f"Smiles: {count}", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    cv2.imshow("Smile Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()