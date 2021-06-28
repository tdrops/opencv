"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

예제 2-6 FPS를 지정해서 동영상 재생
"""
import cv2


video_file = "../img/big_buck.avi"
cap = cv2.VideoCapture(video_file)

if cap.isOpened():

    fps = cap.get(propId=cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)

    print(f"fps:{fps}")

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(winname="cam", mat=img)
            if cv2.waitKey(delay=delay) != -1:
                break
        else:
            break
else:
    print(f"{video_file} open error")

cap.release()
cv2.destroyAllWindows()
