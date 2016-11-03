import cv2
import numpy as np

cap = cv2.VideoCapture(0)

hue = 60
hue_range = 15

picture_hue = 0

ret, frame = cap.read()
rows, cols, channels = frame.shape
resized = (cols//2, rows//2)

picture_shape = (rows//2, cols//2, channels)
picture = np.zeros(picture_shape, dtype=np.uint8)
prev_point = None

while 1:
    ret, frame = cap.read()

    frame = cv2.resize(frame, resized)
    frame = cv2.flip(frame, 1)
    blurred = cv2.medianBlur(frame, 9)
    hsv_im = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    isolated_hue = cv2.inRange(hsv_im, (hue-hue_range, 60, 60), (hue+hue_range, 255, 255))

    _, contours, hierarchy = cv2.findContours(isolated_hue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    thresh = 200
    filtered = [cnt for cnt in contours if cv2.contourArea(cnt) > thresh]

    if len(filtered) is not 0:
        cnt = max(filtered, key=cv2.contourArea)
        (x, y), r = cv2.minEnclosingCircle(cnt)
        x, y, r = map(round, [x, y, r])
        cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
        if prev_point is not None:
            picture_hue = (1 + picture_hue) % 180
            cv2.line(picture, prev_point, (x, y), (picture_hue, 255, 255), 3)
        prev_point = (x, y)
    else:
        prev_point = None

    picture_bgr = cv2.cvtColor(picture, cv2.COLOR_HSV2BGR)
    ret, mask = cv2.threshold(picture[:, :, 1], 50, 255, cv2.THRESH_BINARY_INV)
    frame = cv2.bitwise_and(frame, frame, mask=mask)
    frame = cv2.add(picture_bgr, frame)
    cv2.imshow("Color Detection", frame)
    cv2.imshow("Thresh", mask)
    key = cv2.waitKey(1) & 255

    if key == ord('c'):
        picture = np.zeros(picture_shape, dtype=np.uint8)
    elif key == ord('q'):
        break

cap.release()
