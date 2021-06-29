"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-7] BGR 에서 HSV 로 변환
"""
import cv2
import numpy as np


red_bgr = np.array([[[0,0,255]]], dtype=np.uint8)
green_bgr = np.array([[[0,255,0]]], dtype=np.uint8)
blue_bgr = np.array([[[255,0,0]]], dtype=np.uint8)
yellow_bgr = np.array([[[0,255,255]]], dtype=np.uint8)
magenta_bgr = np.array([[[255,0,255]]], dtype=np.uint8)
cyan_bgr = np.array([[[255,255,0]]], dtype=np.uint8)
orange_bgr = np.array([[[0,125,255]]], dtype=np.uint8)
indigo_bgr = np.array([[[130,0,75]]], dtype=np.uint8)
violet_bgr = np.array([[[255,0,125]]], dtype=np.uint8)

red_hsv = cv2.cvtColor(src=red_bgr, code=cv2.COLOR_BGR2HSV)
green_hsv = cv2.cvtColor(src=green_bgr, code=cv2.COLOR_BGR2HSV)
blue_hsv = cv2.cvtColor(src=blue_bgr, code=cv2.COLOR_BGR2HSV)
yellow_hsv = cv2.cvtColor(src=yellow_bgr, code=cv2.COLOR_BGR2HSV)
magenta_hsv = cv2.cvtColor(src=magenta_bgr, code=cv2.COLOR_BGR2HSV)
cyan_hsv = cv2.cvtColor(src=cyan_bgr, code=cv2.COLOR_BGR2HSV)

orange_hsv = cv2.cvtColor(src=orange_bgr, code=cv2.COLOR_BGR2HSV)
indigo_hsv = cv2.cvtColor(src=indigo_bgr, code=cv2.COLOR_BGR2HSV)
violet_hsv = cv2.cvtColor(src=violet_bgr, code=cv2.COLOR_BGR2HSV)

print(f"red_hsv:{red_hsv}")
print(f"green_hsv:{green_hsv}")
print(f"blue_hsv:{blue_hsv}")
print(f"yellow_hsv: {yellow_hsv}")
print(f"magenta_hsv: {magenta_hsv}")
print(f"cyan_hsv: {cyan_hsv}")
print(f"orange_hsv: {orange_hsv}")
print(f"indigo_hsv: {indigo_hsv}")
print(f"violet_hsv: {violet_hsv}")
