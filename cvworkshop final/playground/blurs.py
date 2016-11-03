import cv2

img = cv2.imread("../images/landscape.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)

mean_blur = cv2.blur(img, (5, 5))
cv2.imshow("Mean Blur", mean_blur)
cv2.waitKey(0)

g_blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Gauss Blur", g_blur)
cv2.waitKey(0)

median_blur = cv2.medianBlur(img, 5)
cv2.imshow("Median Blur", median_blur)
cv2.waitKey(0)

"""
Maintains edges
<img> <diameter> <sigmaColor> <sigmaSpace>
How far the effects range, smaller sigma has less effect
The first argument sigma color specifies how close two pixels have to be in color in order for them to be blurred
higher value -> more blur
The second argument sigma distance is pretty much the same thing as the radius, higher value means more blur
it's a way to measure how many other pixels the current pixel will take into account when blurring
"""
bilateral_blur = cv2.bilateralFilter(img, 31, 40, 150)
cv2.imshow("Bilateral Blur", bilateral_blur)
cv2.waitKey(0)
