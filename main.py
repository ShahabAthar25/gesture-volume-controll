import cv2

camera_width, camera_height = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, camera_width)
cap.set(4, camera_height)

while True:
    success, img = cap.read()

    cv2.imshow("Gesture Volume Control", img)

    key = cv2.waitKey(1)

    if key == 27:
        break