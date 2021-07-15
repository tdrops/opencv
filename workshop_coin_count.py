"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-19] 동전 개수 세기 워크숍 풀이
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/coins_connected.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(src=gray, ksize=(3, 3), sigmaX=0)

circles = cv2.HoughCircles(image=blur, method=cv2.HOUGH_GRADIENT, dp=1.1, minDist=30, circles=None, param1=200)
cnt = 0
if circles is not None:
    # circles = np.uint16(np.around(circles))
    circles = np.round(circles)
    circles = np.int32(circles)
    for i in circles[0, :]:
        cnt += 1
        cv2.circle(img=img, center=(i[0], i[1]), radius=i[2], color=(0, 255, 0), thickness=2)
        # cv2.circle(img=img, center=(i[0], i[1]), radius=2, color=(0,0,255), thickness=5)

        cv2.putText(img=img, text=f"{cnt} r:{i[2]}", org=(i[0], i[1]), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                    color=(0, 0, 255), thickness=1)

    print(circles)
    print(f"동전: {circles.shape[1]}개")
else:
    print("동전: 0개")

cv2.imshow(winname="coin", mat=img)

cv2.waitKey()
cv2.destroyAllWindows()
