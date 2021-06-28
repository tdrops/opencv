"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

예제 2-3 컬러 이미지를 그레이 스케일로 저장
"""
import cv2


filename = "../img/girl.jpg"
img = cv2.imread(filename=filename, flags=cv2.IMREAD_GRAYSCALE)
cv2.imshow(winname=filename, mat=img)
cv2.imwrite(filename="../img/girl_gray.jpg", img=img)
cv2.waitKey()
cv2.destroyAllWindows()
