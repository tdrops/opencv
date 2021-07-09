"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-8] 마우스의 원근 변환으로 문서 스캔 효과 내기
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/paper.jpg")
draw = img.copy()
cv2.imshow(winname="original", mat=draw)

click_cnt = 0
pts = np.zeros(shape=(4,2), dtype=np.float32)


def onMouse(event,x,y,flags,param):
    global click_cnt, pts

    if event == cv2.EVENT_LBUTTONDOWN:
        pts[click_cnt] = [x,y]
        print(pts)
        click_cnt += 1
        cv2.circle(img=draw, center=(x,y), radius=1, color=(0,255,0), thickness=-1)
        cv2.cv2.imshow(winname="original", mat=draw)

        if click_cnt >= 4:
            sm = np.sum(a=pts, axis=1)
            left_up = pts[np.argmin(a=sm)]
            right_down = pts[np.argmax(a=sm)]

            diff = np.diff(a=pts, axis=1)

            right_up = pts[np.argmin(a=diff)]
            left_down = pts[np.argmax(a=diff)]

            x_min = pts[:,0].min()
            x_max = pts[:,0].max()
            y_min = pts[:,1].min()
            y_max = pts[:,1].max()

            w = x_max - x_min
            h = y_max - y_min

            pts1 = np.float32([left_up,left_down,right_up,right_down])
            pts2 = np.float32([[0,0],[0,h],[w,0],[w,h]])

            m = cv2.getPerspectiveTransform(src=pts1, dst=pts2)
            result = cv2.warpPerspective(src=img, M=m, dsize=(x_max-x_min,y_max-y_min))
            cv2.imshow(winname="result", mat=result)
            cv2.waitKey()
            cv2.destroyAllWindows()


cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
