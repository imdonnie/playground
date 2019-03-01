import cv2
import numpy

# print("run in vscode")

frame1_handle = cv2.imread('frames/f1.png')
frame1_array = frame1_handle.item(720, 1280, 3)
print(frame1_array)