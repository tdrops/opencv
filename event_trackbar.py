"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-19] 트랙바를 이용한 이미지 색 조정
"""
import cv2


filename = "../img/blank_500.jpg"
img = cv2.imread(filename=filename)

cv2.imshow(winname=filename, mat=img)

def onChange(x):
    r = cv2.getTrackbarPos(trackbarname="R", winname=filename)
    g = cv2.getTrackbarPos(trackbarname="G", winname=filename)
    b = cv2.getTrackbarPos(trackbarname="B", winname=filename)

    img[:,:] = (b,g,r)
    cv2.imshow(winname=filename, mat=img)


cv2.createTrackbar("R", filename, 255, 255, onChange)
cv2.createTrackbar("G", filename, 255, 255, onChange)
cv2.createTrackbar("B", filename, 255, 255, onChange)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
