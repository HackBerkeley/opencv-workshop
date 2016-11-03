import cv2
import utils_mac as utils
import pyautogui as pa
import time

def close_enough(x, y):
    return abs(x - y) < 20

prev_cacti = []
min_speed = 50
speed = 50
last_time = time.time()

while pa.position() != (0, 0):
    cur_time = time.time()
    img = utils.capture_screen(x1=580, y1=420, x2=1028, y2=477)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 5)
    ret, thresh = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY_INV)
    im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    cacti = []
    shifts = []

    for cnt in contours:
        if cv2.contourArea(cnt) > 80:
            rect = cv2.boundingRect(cnt)
            cacti.append(rect)
            x, y, w, h = rect
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            for px, py, pw, ph in prev_cacti:
                if x < px and close_enough(w*h, pw*ph):
                    shift = px - x
                    shifts.append(shift)

    prev_cacti = cacti
    if len(shifts) > 0:
        speed = (2*speed + sum(shifts) / len(shifts)) / 3
        speed = speed if speed > min_speed else min_speed

    safe_zone = speed * 3.1

    if any([x for x, y, w, h in cacti if x < safe_zone]):
        utils.hit_space()

    last_time = cur_time
    cv2.imshow("T-Rex Runner", img)
    cv2.waitKey(1)