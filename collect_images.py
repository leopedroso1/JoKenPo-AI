# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:28:42 2020

@author: Leonardo

How to Run: On IPython terminal type: python gather_images.py <label_name> <num_samples>

Example: python gather_images.py rocks 200 / python gather_images.py paper 200 / python gather_images.py scisors 200
    
The script will collect <num_samples> number of images and store them
in its own directory.


Only the portion of the image within the box displayed will be captured and stored.

Press 's' to start/pause the image collecting process.
Press 'q' to quit.

"""

import cv2
import os
import sys


# 1. Set up the folder structure 

# Collect arguments from user // Change here
try:

    label_name = sys.argv[1] 
    num_samples = int(sys.argv[2])

except:

    print("Arguments missing. Please use the following structure:\n")
    print("python gather_images.py <label_name> <num_samples>")
    exit(-1)

IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

try:

    os.mkdir(IMG_SAVE_PATH)

except FileExistsError:

    pass

try:

    os.mkdir(IMG_CLASS_PATH)

except FileExistsError:
    print("{} directory already exists.".format(IMG_CLASS_PATH))
    print("All images gathered will be saved along with existing items in this folder")


# 2. Video Capture --> Collects all training images
cap = cv2.VideoCapture(0)

start = False
count = 0

while True:

    ret, frame = cap.read()

    if not ret:

        continue

    if count == num_samples:

        break

    # Area for positioning your hand
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

    if start:
        
        # ROI from the frame
        roi = frame[100:500, 100:500]

        save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(count + 1))

        cv2.imwrite(save_path, roi)

        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, "Collecting {}".format(count),

                (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)

    if k == ord('s'):

        start = not start

    if k == ord('q'):

        break

print("\n{} image(s) saved to {}".format(count, IMG_CLASS_PATH))

cap.release()

cv2.destroyAllWindows()