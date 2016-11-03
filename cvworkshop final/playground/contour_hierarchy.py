import cv2

"""
Contour hierarchies can tell us how the contours are nested.

A contour's child is any contour that is contained within the parent contour
A contour X is a child of a contour Y if X is contained within Y
The child of a contour is a contour that is inside the parent contour

OpenCV contour hierarchy is a list of lists that look like this:
[next, previous, child, parent]

All of these values are just the index of the next contour in our tree.
The 'next' and 'previous' indexes tell us the index of the next contour at our current nesting level
Each index of the hierarchy corresponds to a contour with the same index in your list of contours

Using this tree you can get sometimes very useful information about
    which contours are contained within which other contours.
"""

img = cv2.imread("../images/heir.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
ret, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


h = hierarchy[0]

print(h)
print()
print()

idx = 0
for idx in range(len(h)):
    print(idx, h[idx])
    imc = img.copy()
    cv2.drawContours(imc, contours, idx, (0, 0, 255), 5)

    cv2.imshow("title", imc)
    cv2.waitKey(0)
