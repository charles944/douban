import cv2
import numpy as np

img=cv2.imread("geet.png")
# cv2.imshow("daddy",img)
# resp=cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(resp)
# cv2.imwrite("canny.png",cv2.Canny(img,100,200))
# cv2.imshow("canny",cv2.imread("canny.png"))
# cv2.waitKey()
# cv2.destroyAllWindows()

# img_1=cv2.imshow("img_1",cv2.imread("canny.png"))
# img_2=cv2.imshow("img_2",cv2.imread("canndy.png"))
# cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.imshow("img",cv2.imread("geet.png",-1))
# cv2.imwrite("geet.jpg",cv2.imread("geet.png"))
# cv2.imshow("geet",cv2.imread("geet.jpg"))

img = cv2.imread("geet.png",0)
# cv2.imshow('geet', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bgr=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
cv2.imshow("gray", gray)
cv2.imshow("bgr",bgr)

# cv2.cvtColor(img,"geet_07.png",cv2.COLOR_GRAY2BGR)
# cv2.imshow("geet_07.png")
# cv2.imwrite("geet_05.png",cv2.Canny(img,600,600))
# cv2.imshow("geet_05",cv2.imread("geet_05.png"))
# cv2.imwrite("geet_06.png",cv2.Canny(img,750,750))
# cv2.imshow("geet_06",cv2.imread("geet_06.png"))
cv2.waitKey()
cv2.destroyAllWindows()