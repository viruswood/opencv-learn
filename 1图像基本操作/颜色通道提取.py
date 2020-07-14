import cv2 as cv

img = cv.imread('data/cat.jpg')
b, g, r = cv.split(img)
img[:, :, 0] = 0
img[:, :, 2] = 0

# print(b)
cv.imshow('cat', img)
cv.waitKey()
cv.destroyAllWindows()
