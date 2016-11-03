import cv2

cap = cv2.VideoCapture(0)

hue = 70
hue_range = 13
points = []

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
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
        points.append((x, y))

    for point0, point1 in zip(points, points[1:]):
        cv2.line(frame, point0, point1, (0, 0, 255), 3)

    """
    if len(points) >= 2:
        for i in range(len(points)-2):
            point0 = points[i]
            point1 = points[i+1]
            cv2.line(frame, point0, point1, (0, 0, 255, 3))
    """

    cv2.imshow("Screen Drawing", frame)
    key = cv2.waitKey(1) & 255

    if key == ord('c'):
        points = []
    elif key == ord('q'):
        break

cap.release()
