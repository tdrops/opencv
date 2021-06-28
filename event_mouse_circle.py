"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-17] 마우스 이벤트로 동그라미 그리기
"""
import cv2


filename = "../img/blank_500.jpg"
img = cv2.imread(filename=filename)

cv2.imshow(winname=filename, mat=img)


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=img, center=(x,y), radius=10, color=(0,0,0), thickness=-1)
        cv2.imshow(winname=filename, mat=img)


cv2.setMouseCallback(window_name=filename, on_mouse=onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
