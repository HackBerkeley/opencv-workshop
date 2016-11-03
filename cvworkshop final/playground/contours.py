import cv2

"""
findContours
drawContours
boundingRect

minEnclosingCircle
archLength
approxPolyDP
matchShapes
convexHull
convexityDefects
hierarchy

Contours, what are they? briefly describe how their found.
findContours takes a single channel image, and some other parameters,
    and returns all the contours in the image as a list of lists of lines
    and a hierarchy tree, and we'll see what that is a little later

Hierarchy tree
    In relation to each other you're probably not going use the
    hierarchy tree too terribly much, but it's really good to know what
    it is and what it contains in case you do need some info from it

"""

img = cv2.imread("../images/contours.jpg")

cv2.imshow("image", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 3)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("thresh", thresh)
cv2.waitKey(0)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

"""
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
"""

"""
approximated_contours = []
for cnt in contours:
    if cv2.contourArea(cnt) < 20:
        continue
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # 1. approx = cv2.convexHull(cnt)
    # 2. hull = cv2.convexHull(cnt, returnPoints=False)
    # 2. defects = cv2.convexityDefects(cnt,hull)
    if len(approx):
        approximated_contours.append(approx)
"""


cv2.imshow("title", img)
cv2.waitKey(0)


"""
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

area = cv2.contourArea(cnt)

x, y, w, h = cv2.boundingRect(cnt)
x, y, r = minEnclosingCircle(cnt)

isContourConvex, convexHull, matchShapes

img = cv2.imread("/Users/jtstog/Downloads/heir1.png")

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, 0)
ret, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

h = hierarchy[0]

idx = 0
for idx in range(len(h)):
    print(idx, h[idx])
    imc = img.copy()
    cv2.drawContours(imc, contours, idx, (0, 0, 255), 5)

    cv2.imshow("title", imc)
    cv2.waitKey(0)
Hierarchy: [next, previous, child, parent]
"""