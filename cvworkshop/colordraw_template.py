import cv2

cap = cv2.VideoCapture(0)
points = []

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
    frame = cv2.flip(frame, 1)

    """
    Blur
    Convert to Hue-Saturation-Value colorspace
    Threshold
    Find contours
    Filter out contours that have too small of an area

    Get the biggest contour by area (if it exists)
    Find the minEnclosingCircle
    Draw the circle
    Append its center to our list of points

    If at least two points exist, draw all the lines that are made by consecutive points in the list
    """

    cv2.imshow("Color Detection", frame)
    key = cv2.waitKey(1) & 255

    if key == ord('c'):
        lines = []
    elif key == ord('q'):
        break

cap.release()
