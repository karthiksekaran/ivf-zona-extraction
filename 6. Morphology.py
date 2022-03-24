import cv2 as cv
import numpy as np
img = cv.imread('Good-Embryo-2.jpg',0)
kernel = np.ones((5,5),np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)

cv.imshow("Erosion", erosion)
cv.waitKey(0)

dilation = cv.dilate(img,kernel,iterations = 1)

cv.imshow("Dilation", dilation)
cv.waitKey(0)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

cv.imshow("Opening", opening)
cv.waitKey(0)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

cv.imshow("Closing", closing)
cv.waitKey(0)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow("Gradient", gradient)
cv.waitKey(0)
cv.imwrite("Gradient-Good-2.jpg", gradient)

tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

cv.imshow("Tophat", tophat)
cv.waitKey(0)

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow("Blackhat", blackhat)
cv.waitKey(0)
