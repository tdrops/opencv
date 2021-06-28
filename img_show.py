import cv2


filename = "./img/girl.jpg"
img = cv2.imread(filename=filename)
if img is None:
    print(f"{filename} open error")
else:
    cv2.imshow(winname=filename, mat=img)
    cv2.waitKey()
    cv2.destroyAllWindows()
