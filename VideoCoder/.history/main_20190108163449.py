import cv2
import numpy

# print("run in vscode")

def get_8x8_Block(x_position, y_position, source_array):
        return 0

frame1_handle, frame2_handle = cv2.imread('frames/f1.png'), cv2.imread('frames/f2.png')
cv2.imshow("f1", frame1_handle)
cv2.imshow("f2", frame2_handle)
cv2.waitKey(0)
cv2.destroyAllWondows