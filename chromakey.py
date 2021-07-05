"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-23] 크로마키 마스킹과 합성
"""
import cv2
import numpy as np

img1 = cv2.imread(filename="../img/man_chromakey.jpg")
img2 = cv2.imread(filename="../img/street.jpg")

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

x = (w2 - w1) // 2
y = h2 - h1

chromakey = img1[:10, :10, :]
offset = 20

hsv_chroma = cv2.cvtColor(src=chromakey, code=cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2HSV)

chroma_h = hsv_chroma[:, :, 0]
lower = np.array([chroma_h.min() - offset, 100, 100])
upper = np.array([chroma_h.max() + offset, 255, 255])

mask = cv2.inRange(src=hsv_img, lowerb=lower, upperb=upper)
mask_inv = cv2.bitwise_not(src=mask)

roi = img2[y:y + h1, x:x + w1]

fg = cv2.bitwise_and(src1=img1, src2=img1, mask=mask_inv)
bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
img2[y:y + h1, x:x + w1] = fg + bg

cv2.imshow(winname="img2", mat=img2)

cv2.waitKey()
cv2.destroyAllWindows()
