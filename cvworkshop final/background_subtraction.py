import cv2

cap = cv2.VideoCapture(0)

img_bg = cv2.imread("images/landscape.jpg")
img_bg = cv2.resize(img_bg, (640, 425))

ret, background = cap.read()
background = cv2.resize(background, (0, 0), fx=0.5, fy=0.5)

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    diff = cv2.absdiff(frame, background)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    gray = cv2.blur(gray, (11, 11))

    ret, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, (5, 5))
    inv_thresh = cv2.bitwise_not(thresh)

    fg = cv2.bitwise_and(frame, frame, mask=thresh)

    rows, cols, channels = frame.shape
    # region of interest
    roi = img_bg[0:rows, 0:cols]
    bg = cv2.bitwise_and(roi, roi, mask=inv_thresh)

    overlayed = cv2.add(fg, bg)

    final = img_bg.copy()
    final[0:rows, 0:cols] = overlayed

    cv2.imshow("Final", final)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Image", frame)
    cv2.imshow("Difference", diff)
    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break
