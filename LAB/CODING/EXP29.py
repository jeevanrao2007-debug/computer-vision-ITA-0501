"""Experiment 29: eye detection with a Haar cascade."""
from pathlib import Path
import cv2


def main():
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    face_cascade = cv2.CascadeClassifier(str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"))
    eye_cascade = cv2.CascadeClassifier(str(Path(cv2.data.haarcascades) / "haarcascade_eye.xml"))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    count = 0
    for x, y, width, height in faces:
        face_gray = gray[y:y + height, x:x + width]
        for eye_x, eye_y, eye_width, eye_height in eye_cascade.detectMultiScale(face_gray, 1.1, 5):
            cv2.rectangle(image, (x + eye_x, y + eye_y), (x + eye_x + eye_width, y + eye_y + eye_height), (0, 255, 0), 2)
            count += 1
    cv2.putText(image, f"Eyes: {count}", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Eye Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()