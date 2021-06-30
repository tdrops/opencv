"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-13] 영상의 사칙 영상
"""
import cv2
import numpy as np


a = np.uint8([[200,50]])
b = np.uint8([[100, 100]])

add1 = a + b
sub1 = a - b
mult1 = a * 2
div1 = a / 3

add2 = cv2.add(src1=a, src2=b)
sub2 = cv2.subtract(src1=a, src2=b)
mult2 = cv2.multiply(src1=a, src2=2)
div2 = cv2.divide(src1=a, src2=3)

print(add1, add2)
print(sub1, sub2)
print(mult1, mult2)
print(div1, div2)
