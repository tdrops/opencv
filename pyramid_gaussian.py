"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-18] 가우시안 이미지 미라미드
"""
import cv2

img = cv2.imread(filename="../img/girl.jpg")

smaller = cv2.pyrDown(src=img)

bigger = cv2.pyrUp(src=img)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="smaller", mat=smaller)
cv2.imshow(winname="bigger", mat=bigger)
cv2.waitKey()
cv2.destroyAllWindows()
