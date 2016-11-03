import cv2
import utils_mac as utils

while utils.mouse_position() != (0, 0):
    img = utils.capture_screen(x1=580, y1=420, x2=1028, y2=477)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 5)
    ret, thresh = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY_INV)
    im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        if cv2.contourArea(cnt) > 80:
            x, y, w, h = cv2.boundingRect(cnt)
            if x < 150:
                utils.hit_space()
