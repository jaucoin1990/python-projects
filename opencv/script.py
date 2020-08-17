import cv2 as cv
import sys

img = cv.imread("galaxy.jpg")
img2 = cv.imread("galaxy.jpg")
img3 = cv.imread("galaxy.jpg")

img[:,:,0] = 0
img_with_border = cv.copyMakeBorder(img, 5, 5, 5, 5, cv.BORDER_CONSTANT, value=)
img2[:,:,1] = 0
img3[:,:,2] = 0


cv.imshow("Galaxy Image", img_with_border)
cv.waitKey(5000)
cv.imshow("Galaxy Image", img2)
cv.waitKey(5000)
cv.imshow("Galaxy Image", img3)
cv.waitKey(5000)

