import cv2
import time

"""
Delete Two:

import utils_win as utils
import utils_linux as utils
import utils_mac as utils

Utils functions:

utils.capture_screen(x1=<top_left x>, y1=<top_left y>, x2=<bottom_right x>, y2=<bottom_right y>)
utils.hit_space()
"""


start_time = time.time()
while time.time() - start_time < 20:
    img = utils.capture_screen(x1=____, y1=____, x2=____, y2=____)
    """
    Convert the image to grayscale
    Blur the image
    Threshold the image
    Find contours using the threshold

    Filtering through the contours could look something like this:
    But you can do it any way you want

    for cnt in contours:
        if cv2.contourArea(cnt) > 80:
            x, y, w, h = cv2.boundingRect(cnt)
            if x < safe_distance_from_dinosaur:
                utils.hit_space()
    """