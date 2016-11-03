import cv2

cat = cv2.imread("../images/cat.jpg")
mask = cv2.imread("../images/mask.jpg")

masked_cat = cv2.bitwise_and(cat, mask)

cv2.imshow("result", masked_cat)
cv2.waitKey(0)

"""
That is only if your mask is a 3 channel image like our input image...
If it has a single channel like in a binary image, which it most often will,
then opencv has a special way for you to do this...
"""

cat = cv2.imread("../images/cat.jpg")
# to load in an image as black and white, we can use the optional argument 0
mask = cv2.imread("../images/mask.jpg", 0)

masked_cat = cv2.bitwise_and(cat, cat, mask=mask)

cv2.imshow("result", masked_cat)
cv2.waitKey(0)


"""
That's pretty much all there is to masks in a general sense,
so why are they useful? let's see if we can put the deal with it glasses on our friend dirks
To do this, we're going to use the cv2.add operation. Which just adds
the values of every pixel together from two images. However, if we were to try to just add the two images together,
we'd get some weird stuff going on. You can try that out for yourself to see.
Instead, we need to use masks.

Al images that we put into the bitwise_and function must be of the same type and size
"""

dirks = cv2.imread("../images/dirks.jpg")
# to load in the alpha channel of a png, we should use the optional argument -1,
# which lets us load an image without changing anything about the image
glasses = cv2.imread("../images/deal with it glasses.png", -1)

b, g, r, alpha = cv2.split(glasses)
glasses = cv2.merge((b, g, r))

# the alpha channel is our mask
ret, inv_mask = cv2.threshold(alpha, 100, 255, cv2.THRESH_BINARY_INV)

# our images have to be of the same shape and type for bitwise_and and cv2.add to take them
# so let's get the shape of dirks
rows, cols, _ = glasses.shape

# then we need to crop out an appropriately sized section of the image to work on
# we'll just take the top left for right now
roi = dirks[0:rows, 0:cols]

# then we apply our mask
roi = cv2.bitwise_and(roi, roi, mask=inv_mask)
# and add our image new dirks image
new_roi = cv2.add(glasses, roi)
# then paste the new cropped image back into our bigger image of dirks
dirks[0:rows, 0:cols] = new_roi

cv2.imshow("Dirks with it", dirks)
cv2.waitKey(0)


"""
Now that we have our glasses on our image, we just need to move them to the correct place
"""

dirks = cv2.imread("../images/dirks.jpg")
glasses = cv2.imread("../images/deal with it glasses.png", -1)

b, g, r, alpha = cv2.split(glasses)
glasses = cv2.merge((b, g, r))

ret, inv_mask = cv2.threshold(alpha, 100, 255, cv2.THRESH_BINARY_INV)

rows, cols, _ = glasses.shape

# lets specify an x and y value for the top left corner of our deal with it glasses
x = 360
y = 200
roi = dirks[y:y+rows, x:x+cols]
roi = cv2.bitwise_and(roi, roi, mask=inv_mask)
new_roi = cv2.add(glasses, roi)
dirks[y:y+rows, x:x+cols] = new_roi

cv2.imshow("Dirks with it", dirks)
cv2.waitKey(0)
