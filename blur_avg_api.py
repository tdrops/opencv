"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-2] 블러 전용 함수로 블러링 적용
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/taekwonv1.jpg")

blur1 = cv2.blur(src=img, ksize=(10,10))

blur2 = cv2.boxFilter(src=img, ddepth=-1, ksize=(10,10))

cv2.imshow(winname="ori/blur1/blur2", mat=np.hstack((img,blur1,blur2)))
cv2.waitKey()
cv2.destroyAllWindows()
