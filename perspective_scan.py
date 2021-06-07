"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

비스듬히 찍은 사진을 평면 스캐너 위에 올려 놓은 것처럼 변환하기
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

click_count = 0  # 마우스 클릭할 때마다 값이 바뀌지 않도록 전역 변수 선언
x1 = 0
x2 = 0
x3 = 0
x4 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0

img = cv2.imread(filename="./img/paper.jpg")  # 비스듬히 찍은 사진
h, w = img.shape[:2]  # 높이, 폭 구함
cv2.imshow(winname="original", mat=img)  # 원본 표시
draw = img.copy()  # 마우스 클릭하면서 표시한 점 등이 표시되지 않도록 원본의 복사본 생성


def onMouse(event, x, y, flags, param):
    global click_count, x1, x2, x3, x4, y1, y2, y3, y4  # 사용되는 변수가 전역 변수임을 선언
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 눌림
        click_count += 1
        if click_count == 1:  # 1번 눌림
            x1 = x
            y1 = y
            cv2.circle(img=img, center=(x1, y1), radius=1, color=(0, 255, 0), thickness=-1)  # 눌림 점 표시
            cv2.imshow(winname="original", mat=img)  # 점을 표시하기 위해 다시 그림
        elif click_count == 2:
            x2 = x
            y2 = y
            cv2.circle(img=img, center=(x2, y2), radius=1, color=(0, 255, 0), thickness=-1)
            cv2.imshow(winname="original", mat=img)
        elif click_count == 3:
            x3 = x
            y3 = y
            cv2.circle(img=img, center=(x3, y3), radius=1, color=(0, 255, 0), thickness=-1)
            cv2.imshow(winname="original", mat=img)
        elif click_count == 4:
            x4 = x
            y4 = y
            cv2.circle(img=img, center=(x4, y4), radius=1, color=(0, 255, 0), thickness=-1)

            x_min = min(x1, x2, x3, x4)  # 최소, 최대값 구함
            x_max = max(x1, x2, x3, x4)
            y_min = min(y1, y2, y3, y4)
            y_max = max(y1, y2, y3, y4)

            x_mid = (x_min + x_max) / 2  # 사각형의 중심 좌표 구함
            y_mid = (y_min + y_max) / 2

            if x1 < x_mid:  # 사각형 중심 좌표로 부터 좌상,좌하,우상,우하 구분
                if y1 < y_mid:
                    x_l_t = x1
                    y_l_t = y1
                else:
                    x_l_b = x1
                    y_l_b = y1
            else:
                if y1 < y_mid:
                    x_r_t = x1
                    y_r_t = y1
                else:
                    x_r_b = x1
                    y_r_b = y1

            if x2 < x_mid:
                if y2 < y_mid:
                    x_l_t = x2
                    y_l_t = y2
                else:
                    x_l_b = x2
                    y_l_b = y2
            else:
                if y2 < y_mid:
                    x_r_t = x2
                    y_r_t = y2
                else:
                    x_r_b = x2
                    y_r_b = y2

            if x3 < x_mid:
                if y3 < y_mid:
                    x_l_t = x3
                    y_l_t = y3
                else:
                    x_l_b = x3
                    y_l_b = y3
            else:
                if y3 < y_mid:
                    x_r_t = x3
                    y_r_t = y3
                else:
                    x_r_b = x3
                    y_r_b = y3

            if x4 < x_mid:
                if y4 < y_mid:
                    x_l_t = x4
                    y_l_t = y4
                else:
                    x_l_b = x4
                    y_l_b = y4
            else:
                if y4 < y_mid:
                    x_r_t = x4
                    y_r_t = y4
                else:
                    x_r_b = x4
                    y_r_b = y4

            pts1 = np.float32([[x_l_t, y_l_t], [x_r_t, y_r_t], [x_l_b, y_l_b], [x_r_b, y_r_b]])  # 좌상,우상,좌하,우하 순으로 나열
            pts2 = np.float32([[x_min, y_min], [x_max, y_min], [x_min, y_max], [x_max, y_max]])  # 최대,최소 값으로 대응점 나열
            matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)  # 대응 행렬 구함
            result = cv2.warpPerspective(src=draw, M=matrix, dsize=(w, h))  # 행렬 반영

            cv2.line(img=img, pt1=(x_l_t,y_l_t), pt2=(x_l_b,y_l_b), color=(0,255,0), thickness=1)  # 귀퉁이 4개의 점을 잇는 선 표시
            cv2.line(img=img, pt1=(x_l_b,y_l_b), pt2=(x_r_b,y_r_b), color=(0,255,0), thickness=1)
            cv2.line(img=img, pt1=(x_r_b,y_r_b), pt2=(x_r_t,y_r_t), color=(0,255,0), thickness=1)
            cv2.line(img=img, pt1=(x_r_t,y_r_t), pt2=(x_l_t,y_l_t), color=(0,255,0), thickness=1)
            cv2.imshow(winname="original", mat=img)  # 점, 점을 잇는 선등을 표시한 이미지 표시

            cv2.imshow(winname="result", mat=result)  # 평면 스캐너로 스캔한 것 처럼 생성된 이미지 보여줌


cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
