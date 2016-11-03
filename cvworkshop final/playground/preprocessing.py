import cv2
import numpy as np

"""
Canny Edge Detection
Morphology - Eroding, Dilating, and morphologyEx
Histogram Equalization
Brightness and Contrast
"""

img = cv2.imread("../images/flower.jpg")

"""Brightness"""
delta = 100
brightened = np.where(img > 255-delta, 255, img + delta)

cv2.imshow("Image", brightened)
cv2.waitKey(0)

"""Contrast"""
delta = 2
contrasted = np.where(img > 255 / delta, 255, img*delta)

cv2.imshow("Image", contrasted)
cv2.waitKey(0)

"""Resizing"""
smaller = cv2.resize(img, (100, 100))
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)

smaller = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)

"""Morphology"""

img = cv2.imread("../images/noise.png", 0)

img = cv2.GaussianBlur(img, (3, 3), 0)

ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

thresh = cv2.erode(thresh, None, iterations=3)

cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

thresh = cv2.dilate(thresh, None, iterations=3)

cv2.imshow("Thresh", thresh)
cv2.waitKey(0)


"""
morphologyEx
cv2.MORPH_OPEN ^ exactly what we just did
cv2.MORPH_CLOSE
"""
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, None, iterations=3)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)


"""
canny(<img>, lower threshold, upper threshold)
It uses the sobel operator we talked about (remember the horizontal and vertical derivative combination)
If a pixel is above the upper threshold, then the pixel is an edge
If a pixel is below the lower threshold, then the pixel is not an edge
If a pixel is between the thresholds, then it will only become an edge pixel if
    it is connected to a pixel that passes the first threshold
"""
img = cv2.imread("../images/flower.jpg")

edges = cv2.Canny(img, 90, 200)
cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)

