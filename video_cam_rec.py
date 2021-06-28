"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-9] 카메라로 녹화하기
"""
import cv2


cap = cv2.VideoCapture(0)

if cap.isOpened():
    width = int(cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT))
    rec_filename = "../img/record.avi"
    fps = 25.4
    fourcc = cv2.VideoWriter_fourcc(*"DIVX")
    out = cv2.VideoWriter(rec_filename, fourcc, fps, (width, height))
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(winname="cam", mat=img)
            out.write(image=img)
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            break
else:
    print("cam open error")

cap.release()
cv2.destroyAllWindows()
