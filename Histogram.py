""""

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Good-Embryo.jpg',0)

# alternative way to find histogram of an image
plt.hist(img.ravel(),256,[0,256])
plt.show()



# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('Good-Embryo.jpg',0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()

"""

# import Opencv
import cv2

# import Numpy
import numpy as np

# read a image using imread
img = cv2.imread('Good-Embryo-2.jpg', 0)

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv2.imshow("Equalized", res)
cv2.imwrite("Histogram-Equalized.jpg",equ)

cv2.waitKey(0)
cv2.destroyAllWindows()
