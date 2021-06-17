"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

스캔한 이미지 외곽선 찾기로 원근 제거
"""
import cv2
import numpy as np

img = cv2.imread(filename="./img/paper.jpg")

points = np.zeros(shape=(4, 2), dtype=np.float32)
xsum = 0
ysum = 0

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)  # 단색으로 변경
gray = cv2.GaussianBlur(src=gray, ksize=(3, 3), sigmaX=0)  # Canny 사용하기 위해 흐릿하게 변경
edge = cv2.Canny(image=gray, threshold1=75, threshold2=200)  # 경계 검출

# cv2.imshow(winname="edge", mat=edge)

_, contours, _ = cv2.findContours(image=edge, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)  # 경계선 검출
# contours = sorted(contours, key=cv2.contourArea, reverse=True)

for contour in contours:
    approx = cv2.approxPolyDP(curve=contour, epsilon=cv2.arcLength(curve=contour, closed=True) * 0.02, closed=True)  # 약간 어긋나는 것은 무시
    if len(approx) == 4:  # 4각형임
        approx = approx.reshape(4, 2)  # 4행 2열로 변경
        for i in range(4):
            xsum += approx[i][0]
            ysum += approx[i][1]

        xmid = xsum / 4  # 중심점 구하기
        ymid = ysum / 4

        lt = [0, 0]
        rt = [0, 0]
        lb = [0, 0]
        rb = [0, 0]
        for index in range(4):  # 좌상,좌하,우상,우하 점 찾기
            if approx[index][0] <= xmid:
                if approx[index][1] <= ymid:
                    lt = approx[index]
                else:
                    lb = approx[index]
            else:
                if approx[index][1] <= ymid:
                    rt = approx[index]
                else:
                    rb = approx[index]

        points1 = np.float32([lt, rt, lb, rb])
        x, y, w, h = cv2.boundingRect(points=points1)  # 경계를 감싸는 사각형 구하기
        points2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        m = cv2.getPerspectiveTransform(src=points1, dst=points2)  # 변환 행렬 구하기
        warp = cv2.warpPerspective(src=img, M=m, dsize=(w, h))  # 변환 행렬 적용
        cv2.imshow(winname="warp", mat=warp)  # 변경된 값 보이기

        break

cv2.waitKey()
cv2.destroyAllWindows()
