import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import the image
img = cv2.imread('images/burano.jpg')

# Convert the image into gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plot the image
plt.imshow(img_gray, cmap = 'gray')
plt.show()

