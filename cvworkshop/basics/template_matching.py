import cv2
import numpy as np


def highlight_roi(image, x, y, w, h):
    rows, cols, _ = image.shape
    mask = np.zeros((rows, cols), dtype=np.uint8)
    mask[y:y+h, x:x+w] = 255
    inv_mask = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(image, image, mask=mask)
    bg = cv2.bitwise_and(image, image, mask=inv_mask)
    bg = (bg * 0.25).astype(np.uint8)
    image = cv2.add(fg, bg)
    return image

"""
Template matching isn't the most versatile technique so
we won't spend to much time on it, but it's simple and
can be quite powerful and reliable under
certain circumstances. If you have the exact sub image that
you're searching for in you search image, then template matching
will let you find that image for you
Let's see if we can find waldo.

So you might think this is cheating since we already have
the exact image we're searching for, but
"""

template = cv2.imread("../images/template_matching/waldo.jpg")
image = cv2.imread("../images/template_matching/search_image.jpg")

cv2.imshow("I found waldo!", image)
cv2.waitKey(0)

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

h, w, _ = template.shape
x, y = max_loc

image = highlight_roi(image, x, y, w, h)

cv2.imshow("Waldo", template)
cv2.waitKey(0)

cv2.imshow("I found waldo!", image)
cv2.waitKey(0)


"""
What if we wanted to read an odometer? We could try to use
machine learning or something complicated...
But template matching is enough!
"""


template = cv2.imread("../images/template_matching/digit8.jpg")
image = cv2.imread("../images/template_matching/odometer.png")

meter = cv2.imread("../images/template_matching/meter.jpg")
meter = cv2.resize(meter, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("Meter", meter)
cv2.waitKey(0)
cv2.imshow("Digit", template)
cv2.waitKey(0)

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

h, w, _ = template.shape
x, y = max_loc

image = highlight_roi(image, x, y, w, h)
image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)


cv2.imshow("Easy digit finding", image)
cv2.waitKey(0)