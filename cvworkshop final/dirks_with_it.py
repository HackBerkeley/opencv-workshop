import cv2

path = 'images/dirks/dirks4.jpg'
im = cv2.imread(path)

im = cv2.bilateralFilter(im, 11, 41, 41)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 5, 70, 3)

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1.2, 50, param1=10, maxRadius=100)

circles = circles[0]

for r, x, y in circles:
    cv2.circle(im, (x, y), r, (0, 0, 255), 3)

cv2.imshow("t1", canny)
cv2.imshow("t", im)
cv2.waitKey(0)
