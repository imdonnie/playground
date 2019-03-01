import cv2
import numpy

# print("run in vscode")

def get_MxN_Block(x_position, y_position, M, N, source_image_array):
    block_array = source_image_array[x_position:x_position+M, y_position:y_position+N,::]
    return block_array

if __name__ == "__main__":
    frame1, frame2 = cv2.imread('frames/f1.png'), cv2.imread('frames/f2.png')
    cv2.imshow("f1", frame1)
    # cv2.imshow("f2", frame2_handle)
    block1 = get_MxN_Block(0, 0, 16, 16, frame1)

    cv2.waitKey(0)
    cv2.destroyAllWondows()