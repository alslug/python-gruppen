#!/usr/bin/python3
'''
Creator : Sten N. Herbst
Date : 2019.07.30
Title: Simple TKinter Class 17-01
'''

import tkinter
import cv2
import PIL.Image, PIL.ImageTk

# Create a window
window = tkinter.Tk()

# Load an image using OpenCV
cv_img = cv2.imread("python01.jpg")

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape

# Run the window loop
window.mainloop()