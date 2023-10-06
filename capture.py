import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capture an image
ret, frame = cap.read()
cv2.imwrite('image.jpg', frame)

# Release the webcam
cap.release()
