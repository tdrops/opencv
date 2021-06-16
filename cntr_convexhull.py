import cv2
import numpy as np


img = cv2.imread(filename="./img/hand.jpg")
img2 = img.copy()

img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret, img_gray = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
temp,contours,hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]

hull = cv2.convexHull(points=contour)
cv2.drawContours(image=img, contours=[hull], contourIdx=-1,color=(0,255,0), thickness=1)

print(cv2.isContourConvex(contour=contour), cv2.isContourConvex(contour=hull))

hull2 = cv2.convexHull(points=contour, returnPoints=False)
defects = cv2.convexityDefects(contour=contour, convexhull=hull2)

for i in range(defects.shape[0]):
    print(defects[i,0])
    startP, endP, farthestP, distance = defects[i,0]
    farthest = tuple(contour[farthestP][0])
    dist = distance/256.0
    if dist > 1:
        cv2.circle(img=img2, center=farthest, radius=3, color=(0, 0, 255), thickness=-1)

cv2.imshow(winname="contour", mat=img)
cv2.imshow(winname="convex hull", mat=img2)

cv2.waitKey()
cv2.destroyAllWindows()
