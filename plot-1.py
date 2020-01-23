import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import the image
img = cv2.imread('images/burano.jpg')

# plot the image
plt.imshow(img)
plt.show()
