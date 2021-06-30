"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-15] 이미지 단순 합성
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="../img/wing_wall.jpg")
img2 = cv2.imread(filename="../img/yate.jpg")

# cv2.imshow(winname="img1+img2", mat=img1+img2)
# cv2.imshow(winname="add(img1,img2)", mat=cv2.add(img1,img2))

cv2.imshow(winname="blending", mat=np.hstack((img1,img2,img1+img2,cv2.add(img1,img2))))

cv2.waitKey()
cv2.destroyAllWindows()
