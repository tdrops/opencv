import cv2
import numpy as np
import matplotlib.pylab as plt


rate = 15

img = cv2.imread(filename="./img/taekwonv1.jpg")
draw = img.copy()
cv2.imshow(winname="original", mat=draw)

while True:
    x,y,w,h = cv2.selectROI(windowName="original", img=img)
    if x > 0 and y > 0:
        roi = img[y:y+h,x:x+w]
        roi = cv2.resize(src=roi, dsize=(w//rate, h//rate))
        roi = cv2.resize(src=roi, dsize=(w, h), interpolation=cv2.INTER_AREA)
        img[y:y+h,x:x+w] = roi
        cv2.imshow(winname="original", mat=img)
    else:
        break

# cv2.waitKey()
cv2.destroyAllWindows()
