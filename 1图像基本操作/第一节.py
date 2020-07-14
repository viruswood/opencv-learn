import cv2 as cv

img = cv.imread('data/cat.jpg', cv.IMREAD_GRAYSCALE)
print(img.shape)
print(img)
cv.imshow('img', img)
cv.imwrite('mycat.png',img)
cv.waitKey(0)
cv.destroyAllWindows()
