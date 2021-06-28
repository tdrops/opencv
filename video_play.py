"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 2-4] 동영상 파일 재생
"""
import cv2


video_file = "../img/big_buck.avi"


cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(winname=video_file, mat=img)
            cv2.waitKey(delay=25)
        else:
            break
else:
    print(f"{video_file} open error")

cap.release()
cv2.destroyAllWindows()
