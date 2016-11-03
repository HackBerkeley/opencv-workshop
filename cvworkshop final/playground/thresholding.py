import cv2

def show_image(im):
    cv2.imshow("Image", im)
    cv2.waitKey(0)

img = cv2.imread('../images/sudoku.jpg')

show_image(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show_image(gray)

"""
cv2.threshold( <img>, <minimum pixel value>, <output pixel value>, <threshold type>)

For every pixel in the image, if the pixel's value is greater
than the <minimum pixel value>, then that pixel gets assigned
the <output pixel value>, otherwise it gets assigned 0

The <threshold type> that you choose will output different styled thresholds.
The two most common threshold types we use will be
"""

return_value, threshold_img = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
show_image(threshold_img)

"""
If you don't know what the best minimum thresholding value is,
you can have OpenCV find it for you by passing in 0 and
adding cv2.THRESH_OTSU to your threshold type. All these cv2.OPTION things are
just numbers by the way.
"""

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
show_image(thresh)

"""
If you have a shadow in the image you're thresholding,
then a global threshold won't help much because you'll only ever get half of your image.
To deal with that we can threshold using kernels, so that we can
threshold on a local basis just inside the kernel, that's called adaptive thresholding.

cv2.adaptiveThreshold(<img>, <output pixel value>, <method>, <threshold type>, <block size>, <constant>)
cv2.ADAPTIVE_THRESH_MEAN_C
cv2.ADAPTIVE_THRESH_GAUSSIAN_C

block size - size of the kernel
The larger the kernel size, the more neighbors the threshold will take into account

constant - subtracted from the average among the pixels in the kernel
"""

adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 3)
show_image(adaptiveThresh)

"""
cv2.inRange
"""
