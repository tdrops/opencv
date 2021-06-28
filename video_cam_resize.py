"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-7] 카메라 프레임 크기 설정
"""
import cv2


cap = cv2.VideoCapture(0)

if cap.isOpened():
    width = cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)

    print(f"width:{width} height:{height}")

    cap.set(propId=cv2.CAP_PROP_FRAME_WIDTH, value=320)
    cap.set(propId=cv2.CAP_PROP_FRAME_HEIGHT, value=240)

    width = cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)

    print(f"width:{width} height:{height}")

    while True:
        ret, img = cap.read()
        cv2.imshow(winname="cam", mat=img)
        if cv2.waitKey(1) != -1:
            break
else:
    print(f"cam open error")
    pass

cap.release()
cv2.destroyAllWindows()
