import cv2
import numpy as np
#load image

img = cv2.imread("Good-3.jpg")

#print original

cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Creating maxican hat filter
filter = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
# Applying cv2.filter2D function on our Logo image
#filter_2 = np.array([[3, -2, -3], [-4, 8, -6], [5, -1, -0]])
filter_2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
mexican_hat_img2=cv2.filter2D(img,-1,filter_2)
cv2.imwrite("Sharpened.jpg",mexican_hat_img2)
cv2.imshow("Sharpened", mexican_hat_img2)
cv2.waitKey(0)

#Image Blur
img_blur = cv2.imread("Sharpened.jpg")
blur = cv2.bilateralFilter(img_blur,50,75,75)
cv2.imshow("Bilateral", blur)
cv2.imwrite("Bilateral.jpg", blur)
cv2.waitKey(0)

#Morphology
kernel = np.ones((5,5),np.uint8)
img_morph = cv2.imread("Bilateral.jpg")
eroded = cv2.morphologyEx(img_morph, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Morphed", eroded)
cv2.imwrite("Morphed.jpg", eroded)
cv2.waitKey(0)

#Edge Detection

from PIL import Image, ImageFilter



#Thresholding
img_binary = cv2.imread("Morphed.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255,
							cv2.THRESH_BINARY +
							cv2.THRESH_OTSU)
cv2.imshow('Thresholded', thresh)
cv2.waitKey(0)