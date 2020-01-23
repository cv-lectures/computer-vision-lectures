import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import the image
img = cv2.imread('images/wall.jpg')

# Copy the image
img_copy = img.copy()

# Draw a rectangle 
cv2.rectangle(img_copy, pt1 = (800, 470), pt2 = (980, 530), 
              color = (255, 0, 0), thickness = 5)

# plot the image copy
plt.imshow(img_copy)
plt.show()

