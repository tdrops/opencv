"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-16] 키 이벤트
"""
import cv2


filename = "../img/girl.jpg"
img = cv2.imread(filename=filename)

cv2.imshow(winname=filename, mat=img)

x = 100
y = 100

cv2.moveWindow(winname=filename, x=x, y=y)

while True:
    key = cv2.waitKey(0) & 0xff
    if key == ord('h'):
        x = x - 10
    elif key == ord('j'):
        y = y + 10
    elif key == ord('k'):
        y = y - 10
    elif key == ord('l'):
        x = x + 10

    elif key == ord('q') or key == 27:
        break

    cv2.moveWindow(winname=filename, x=x, y=y)

cv2.destroyAllWindows()





