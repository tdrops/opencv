import cv2
import numpy as np

img = cv2.imread(filename="../img/fish.jpg")
h, w = img.shape[:2]

pts1 = np.float32([[100, 50], [200, 50], [100, 200]])
pts2 = np.float32([[80, 70], [210, 60], [250, 120]])

cv2.circle(img=img, center=(100, 50), radius=5, color=(255, 0, 0), thickness=-1)
cv2.circle(img=img, center=(200, 50), radius=5, color=(0, 255, 0), thickness=-1)
cv2.circle(img=img, center=(100, 200), radius=5, color=(0, 0, 255), thickness=-1)

mtrx = cv2.getAffineTransform(src=pts1, dst=pts2)
result = cv2.warpAffine(src=img, M=mtrx, dsize=(w, h))

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
