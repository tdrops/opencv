"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

pyrMeanShiftFiltering - 포스터 처럼 색칠
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/taekwonv1.jpg")

def onChange(x):
    sp = cv2.getTrackbarPos("sp",  winname="original")
    sr = cv2.getTrackbarPos("sr",  winname="original")
    lv = cv2.getTrackbarPos("lv",  winname="original")

    mean = cv2.pyrMeanShiftFiltering(src=img, sp=sp, sr=sr, dst=None, maxLevel=lv)
    cv2.imshow(winname="original", mat=np.hstack([img, mean]))

cv2.imshow(winname="original", mat=np.hstack([img, img]))

cv2.createTrackbar("sp", "original", 0, 100, onChange)
cv2.createTrackbar("sr", "original", 0, 100, onChange)
cv2.createTrackbar("lv", "original", 0, 5, onChange)

cv2.waitKey()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# img = cv2.imread('../img/taekwonv1.jpg')
# # 트랙바 이벤트 처리 함수
# def onChange(x):
#     #sp, sr, level 선택 값 수집
#     sp = cv2.getTrackbarPos('sp', 'img')
#     sr = cv2.getTrackbarPos('sr', 'img')
#     lv = cv2.getTrackbarPos('lv', 'img')
#
#     # 평균 이동 필터 적용 ---①
#     mean = cv2.pyrMeanShiftFiltering(img, sp, sr, None, lv)
#     # 변환 이미지 출력
#     cv2.imshow('img', np.hstack((img, mean)))
#
# # 초기 화면 출력
# cv2.imshow('img', np.hstack((img, img)))
# # 트랙바 이벤트 함수 연결
# cv2.createTrackbar('sp', 'img', 0,100, onChange)
# cv2.createTrackbar('sr', 'img', 0,100, onChange)
# cv2.createTrackbar('lv', 'img', 0,5, onChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
