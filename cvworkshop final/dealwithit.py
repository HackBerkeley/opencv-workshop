import cv2
import math
import numpy as np

eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

glasses_raw = cv2.imread('images/deal with it.png', -1)

cap = cv2.VideoCapture(0)

old_eye_centers = None
distance = lambda p0, p1: ((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)**0.5

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.equalizeHist(gray)
    cv2.imshow("Hist", gray)

    face = face_cascade.detectMultiScale(gray, 1.3)

    if len(face) == 0:
        continue
    x, y, w, h = face[0]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (00, 255, 0), 3)
    roi = frame[y+h:x+w]

    eyes = eye_cascade.detectMultiScale(roi)
    print(eyes)
    eyes = [(x+relative_x, y+relative_y, w, h) for relative_x, relative_y, w, h in eyes]

    eye_centers = []
    for x, y, w, h in eyes:
        center = (x + w//2, y + h//2)
        eye_centers.append(center)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 6)

    if len(eye_centers) != 2 and old_eye_centers is not None:
        eye_centers = old_eye_centers

    if len(eye_centers) == 2:
        old_eye_centers = eye_centers
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
        glasses_width = eye_distance * 210 // 80
        r, c, _ = glasses_raw.shape
        glasses_height = glasses_width * r // c
        resized_glasses = cv2.resize(glasses_raw, (glasses_width, glasses_height), interpolation=cv2.INTER_CUBIC)

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
        except cv2.error as e:
            print(e)

    cv2.imshow("Deal with it", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
