"""Experiment 38: count faces in an image."""
from pathlib import Path
import cv2


def count_faces(image):
    cascade = cv2.CascadeClassifier(str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))


def main():
    folder = Path(__file__).resolve().parent
    path = folder / "INPUT.jpeg" if (folder / "INPUT.jpeg").exists() else folder / "image.jpeg"
    image = cv2.imread(str(path))
    if image is None:
        print(f"Error: Could not load {path}.")
        return
    faces = count_faces(image)
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
    print(f"Number of faces: {len(faces)}")
    cv2.putText(image, f"Faces: {len(faces)}", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Face Count", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()