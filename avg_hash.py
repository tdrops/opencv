"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

평균 해시 만들기
"""
import cv2
import numpy


img = cv2.imread(filename="./img/pistol.jpg")
cv2.imshow(winname="original", mat=img)

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow(winname="gray", mat=gray)

rsize = cv2.resize(src=gray, dsize=(16,16))
cv2.imshow(winname="rsize", mat=rsize)

print(rsize)
avg = rsize.mean()
print(avg)
bin = (rsize > avg)*1
print(bin)

cv2.waitKey()
cv2.destroyAllWindows()
