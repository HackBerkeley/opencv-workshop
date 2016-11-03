import cv2
import math
import numpy as np
import threading
import os
import time

music_playing = False
threads = []


def detect_colors(img):
    hue = 70
    hue_range = 5
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = cv2.medianBlur(hsv, 21)
    lower = (hue-hue_range, 100, 100)
    upper = (hue+hue_range, 255, 255)
    isolated = cv2.inRange(hsv, lower, upper)
    isolated = cv2.morphologyEx(isolated, cv2.MORPH_OPEN, (11, 11))
    cv2.imshow("iso", isolated)
    _, contours, heir = cv2.findContours(isolated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >= 2:
        contours = sorted(contours, key=cv2.contourArea)[::-1][:2]
    rects = [cv2.boundingRect(cnt) for cnt in contours]
    return rects

colors = [
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0)
]

color_choice = 0

music_start = None

face_cascade = cv2.CascadeClassifier('face_haarcascade.xml')

glasses_raw = cv2.imread('images/deal with it.png', -1)

cap = cv2.VideoCapture(0)

eye_centers = []

continuous_frames = 0

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    face = face_cascade.detectMultiScale(gray, 1.3)

    if len(face) != 0:
        x, y, w, h = face[0]
        cv2.rectangle(gray, (x, y), (x+w, y+h), (00, 255, 0), 3)
        cv2.imshow("Gray", gray)
        roi = frame[y:y+h, x:x+w]

        eyes = detect_colors(roi)
        eyes = [(x+x1, y+y1, w, h) for x1, y1, w, h in eyes]

        eye_centers = []
        for x, y, w, h in eyes:
            center = (x + w//2, y + h//2)
            eye_centers.append(center)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 6)

    if len(eye_centers) == 2:
        eye1, eye2 = eye_centers
        last_left = eye2
        last_right = eye1
        x1, y1 = eye1
        x2, y2 = eye2
        opposite = y2 - y1
        adjancent = x2 - x1
        midpoint = last_midpoint = ((x1+x2)//2, (y1+y2)//2)

        """Scale the glasses"""
        eye_distance = int(math.sqrt(opposite**2 + adjancent**2))
        glasses_width = eye_distance * 210 // 100
        r, c, _ = glasses_raw.shape
        glasses_height = glasses_width * r // c
        try:
            resized_glasses = cv2.resize(glasses_raw, (glasses_width, glasses_height), interpolation=cv2.INTER_CUBIC)
        except cv2.error as e:
            continue

        """Get the angle of our head"""
        head_angle = -180 * np.arctan(opposite/adjancent) / math.pi

        """Rotate the glasses"""
        rows, cols, _ = resized_glasses.shape
        M = cv2.getRotationMatrix2D((cols//2, rows//2), head_angle, 1)
        rotated_glasses = cv2.warpAffine(resized_glasses, M, (cols, rows))

        finished_glasses = rotated_glasses

        """ Overlay the image """
        rows, cols, _ = finished_glasses.shape
        x, y = midpoint[0], midpoint[1]
        x -= cols//2
        y -= rows//2

        b, g, r, alpha = cv2.split(finished_glasses)
        ret, thresh = cv2.threshold(alpha, 20, 255, 0)

        finished_glasses = cv2.merge((b, g, r))

        mask = thresh
        inv_mask = cv2.bitwise_not(mask)

        roi = frame[y:y+rows, x:x+cols]
        try:
            bg = cv2.bitwise_and(roi, roi, mask=inv_mask)
            fg = cv2.bitwise_and(finished_glasses, finished_glasses)
            combined = cv2.add(fg, bg)
            frame[y:y+rows, x:x+cols] = combined
            rows, cols, _ = frame.shape
            continuous_frames += 1
            if music_playing and music_start and time.time() - music_start > 5:
                color_choice = (color_choice+1) % 3
                frame = cv2.putText(frame, "Deal With It", (cols//2-30, rows-20), cv2.FONT_HERSHEY_SIMPLEX, 2, colors[color_choice], 5)
            if not music_playing and continuous_frames >= 10:
                music_playing = True
                music_start = time.time()
                thread = threading.Thread(target=os.system, args=("afplay /Users/jtstog/Downloads/dealwithitsong.mov",))
                thread.start()
                threads.append(thread)
        except cv2.error as e:
            pass
    else:
        continuous_frames = 0

    cv2.imshow("Deal with it", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
exit()