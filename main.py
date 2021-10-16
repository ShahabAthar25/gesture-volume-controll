from modules import hand_detection as hand
import cv2
import time

camera_width, camera_height = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, camera_width)
cap.set(4, camera_height)

current_time = 0
previous_time = 0

detector = hand.hand_detector()

while True:
    success, img = cap.read()

    img = detector.find_hand(img)

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)

    cv2.imshow("Gesture Volume Control", img)

    key = cv2.waitKey(1)

    if key == 27:
        break