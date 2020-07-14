import cv2 as cv

vc = cv.VideoCapture('data/test.mp4')
if vc.isOpened():
    open, frame = vc.read()
else:
    open = False
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('resut', gray)
        if cv.waitKey(10) & 0xFF == 27:
            break
vc.release()
cv.destroyAllWindows()