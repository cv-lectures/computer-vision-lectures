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

# Draw a circle 
cv2.circle(img_copy, center = (950, 50), radius = 50, 
           color = (0, 0, 255), thickness = 5)

# Add text 
cv2.putText(img_copy, text = "the Wall of Love", 
            org = (250, 250),
            fontFace = cv2.FONT_HERSHEY_DUPLEX, 
            fontScale = 2, 
            color = (0, 255, 0), 
            thickness = 2, 
            lineType = cv2.LINE_AA)

# plot the image copy
plt.imshow(img_copy)
plt.show()
