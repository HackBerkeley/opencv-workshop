import cv2


img = cv2.imread("../images/color wheel.jpg")

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", img)
cv2.waitKey(0)

""""""

img = cv2.imread("../images/color wheel.jpg")

# go to image to find coordinates
print(img[250, 100])
cv2.imshow("image", img)
cv2.waitKey(0)

""""""

img = cv2.imread("../images/color wheel.jpg")

b, g, r = cv2.split(img)

b[:] = 0
img = cv2.merge((b, g, r))

# same thing as img[:, :, 0] = 0

cv2.imshow("Merged", img)
cv2.waitKey(0)

""""""

img = cv2.imread("../images/color wheel.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv[250, 100])
