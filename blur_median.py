"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-4] 미디언 블러링
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/salt_pepper_noise.jpg")

blur = cv2.medianBlur(src=img, ksize=5)

cv2.imshow(winname="ori/blur", mat=np.hstack((img,blur)))
cv2.waitKey()
cv2.destroyAllWindows()
