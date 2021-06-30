"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-6] 50% 알파 블렌딩
"""
import cv2
import numpy as np

alpha = 0.5

img1 = cv2.imread(filename="../img/wing_wall.jpg")
img2 = cv2.imread(filename="../img/yate.jpg")


add1 = np.uint8(img1 * alpha + img2 * (1-alpha))
add2 = cv2.addWeighted(src1=img1, alpha=alpha, src2=img2, beta=(1-alpha), gamma=0)

cv2.imshow(winname="add", mat=np.hstack((img1,img2,add1,add2)))
cv2.waitKey()
cv2.destroyAllWindows()
