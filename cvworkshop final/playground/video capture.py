import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()

    cv2.imshow("Video Camera Testing", frame)
    key = cv2.waitKey(1) & 255
    if key == ord('q'):
        break

cap.release()

""""""

cap = cv2.VideoCapture(0)

ret, first = cap.read()

while 1:
    ret, frame = cap.read()

    new_frame = cv2.absdiff(frame, first)
    first = frame

    cv2.imshow("Frame", new_frame)
    key = cv2.waitKey(1) & 255
    if key == ord('q'):
        break

cap.release()
