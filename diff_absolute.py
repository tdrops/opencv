"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-20] 차영상으로 도면의 차이 찾아내기
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="../img/robot_arm1.jpg")
img2 = cv2.imread(filename="../img/robot_arm2.jpg")

gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(src1=gray1, src2=gray2)
_,diff = cv2.threshold(src=diff, thresh=1, maxval=255, type=cv2.THRESH_BINARY)
diff_red = cv2.cvtColor(src=diff, code=cv2.COLOR_GRAY2BGR)
diff_red[:,:,2] = 0

spot = cv2.bitwise_xor(src1=img2, src2=diff_red)

cv2.imshow(winname="img1", mat=img1)
cv2.imshow(winname="img2", mat=img2)
cv2.imshow(winname="diff", mat=diff)
cv2.imshow(winname="spot", mat=spot)
cv2.waitKey()
cv2.destroyAllWindows()
