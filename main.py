from modules import hand_detection as hand
import alsaaudio
import cv2
import time
import math

camera_width, camera_height = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, camera_width)
cap.set(4, camera_height)

current_time = 0
previous_time = 0

detector = hand.hand_detector(detection_cofidence=0.9)

while True:
    success, img = cap.read()

    img = detector.find_hand(img)

    landmarks = detector.get_landmark(img, draw=False)

    if len(landmarks) != 0:
        
        x1, y1 = landmarks[4][1], landmarks[4][2]
        x2, y2 = landmarks[8][1], landmarks[8][2]

        cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (0, 0, 255), cv2.FILLED)

        cv2.line(img, (x1, y1),(x2, y2), (0, 0, 255), 3)

        lenght = math.hypot(x1 - x2, y2 - y1)

        if lenght > 300:
            lenght = 300

        lenght_percentage = lenght/300 * 100
        lenght_percentage = int(lenght_percentage)

        m = alsaaudio.Mixer()
        vol = m.getvolume()
        m.setvolume(lenght_percentage)
        print(vol)

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)

    cv2.imshow("Gesture Volume Control", img)

    key = cv2.waitKey(1)

    if key == 27:
        break