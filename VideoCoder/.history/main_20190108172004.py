import cv2
import numpy

# print("run in vscode")

# get a N*N block from a source image
def get_NxN_Block(x_position, y_position, N, source_image):

    if x_position*y_position*N < 0:
        return "Invalid Args"

    source_height, source_width, _ = source_image.shape()
    if x_position+N > source_width or y_position+N > source_height:
        return "Args out of size"

    block_array = source_image[y_position:y_position+N, x_position:x_position+N, ::]
    return block_array

# slice a source image into many blocks
def sliceImage(N, source_image):
    source_height, source_width, _ = source_image.shape
    blocks = []
    positions = []
    for i in range(source_width//N):
        for j in range(source_height//N):
            positions.append([i*N, j*N])
    print(positions)

if __name__ == "__main__":
    frame1, frame2 = cv2.imread('frames/f1.png'), cv2.imread('frames/f2.png')
    cv2.imshow("f1", frame1)
    print(frame1.shape)
    sliceImage(120, frame1)
    # cv2.imshow("f2", frame2_handle)
    # block1 = get_MxN_Block(512, 512, 256, 256, frame1)

    # cv2.imshow('b1', block1)

    cv2.waitKey(0)
    cv2.destroyAllWondows()