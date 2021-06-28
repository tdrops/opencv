"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

예제 2-5 카메라 프레임 읽기
"""
import cv2


cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(winname="cam", mat=img)
            if cv2.waitKey(1) != -1:
                break
        else:
            break
else:
    print(f"cam open error")

cap.release()
cv2.destroyAllWindows()
