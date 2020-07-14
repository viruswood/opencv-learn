import cv2 as cv
img = cv.imread('data/cat.jpg')
cat = img[0:200,0:200]
cv.imshow('cat',cat)
cv.waitKey()
cv.destroyAllWindows()