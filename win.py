"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-15] 창 관리 API 사용하기
"""
import cv2


filename = "../img/girl.jpg"
img = cv2.imread(filename=filename)
img_gray = cv2.imread(filename=filename, flags=cv2.IMREAD_GRAYSCALE)

cv2.namedWindow(winname="origin", flags=cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(winname="gray", flags=cv2.WINDOW_NORMAL)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="gray", mat=img_gray)

cv2.waitKey(0)

cv2.moveWindow(winname="origin", x=0, y=0)
cv2.moveWindow(winname="gray", x=100, y=100)

cv2.waitKey(0)

cv2.resizeWindow(winname="origin", width=200, height=200)
cv2.resizeWindow(winname="gray", width=100, height=100)

cv2.waitKey(0)

cv2.destroyAllWindows()
