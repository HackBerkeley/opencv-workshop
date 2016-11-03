import cv2
import numpy as np

"""
Lines, circles, arcs, polygons,

line:
image, point1, point2, color, thickness

rectangle
image, top left, bottom right, color, thickness

circle:
image, center, radius, color, thickness

putText
Image, Text, bottom left point, Font, Font Scale, Color, Thickness

polygon
image, [points], True, color
"""

w, h = 500, 500

drawing = np.zeros((w, h, 3), np.uint8)

cv2.circle(drawing, (w//2, h//2), w//3, (0, 255, 0), 5)

cv2.circle(drawing, (w//2 - 60, h//2 - 45), 20, (255, 0, 0), -1)
cv2.circle(drawing, (w//2 + 60, h//2 - 45), 20, (255, 0, 0), -1)

x, y = w//2 - 75, h//2 - 80
cv2.line(drawing, (x, y), (x+200, y), (0, 0, 255), 5)

cv2.rectangle(drawing, (220, 300), (280, 320), (100, 100, 100), 3)

cv2.putText(drawing, "Hello World", (30, h-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

pts = np.array([[[10, 10]],
                [[30, 15]],
                [[100, 90]],
                [[50, 200]]
                ], np.int32)

cv2.polylines(drawing, [pts], True, (0, 255, 255))

cv2.imshow("My Pretty Picture", drawing)
cv2.waitKey(0)
