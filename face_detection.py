# -*- coding: utf-8 -*-
"""face_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dY8qfRyut5j1TreDrho0FCWKOwYUhABM

Face Detection using OpenCV
"""

import cv2  # OpenCV for computer vision
import numpy as np  # NumPy for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for displaying images

# Load the image
image = cv2.imread("/content/OpenCV_img.png")

# Convert from BGR to RGB (OpenCV loads images in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.axis('off')  # Hide axes
plt.show()

!wget -O haarcascade_frontalface_default.xml https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Convert the image to grayscale (Haar cascade works better on grayscale images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Print number of faces detected
print(f"Number of faces detected: {len(faces)}")

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle

# Display the image with detected faces
plt.imshow(image_rgb)
plt.axis("off")
plt.show()