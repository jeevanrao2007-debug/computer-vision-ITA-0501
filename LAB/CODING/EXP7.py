import cv2

# Load video file (use 0 for live webcam input)
cap = cv2.VideoCapture('video.mp4')

if not cap.isOpened():
    print("Error opening video stream or file")

# Select mode: 1 = Normal, 2 = Slow Motion, 3 = Fast Motion
mode = 2  

# Set delay in milliseconds per frame based on mode
if mode == 1:
    delay = 30   # Normal
elif mode == 2:
    delay = 100  # Slow motion (slower playback)
elif mode == 3:
    delay = 5    # Fast motion (faster playback)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video Playback', frame)

    # Press 'q' on keyboard to exit video playback
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
