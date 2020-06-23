import numpy as np
import cv2

geet=cv2.imread("geet.png")
# print(geet.size)
# print(geet.shape)
# img=np.zeros((315,559))
# # print(img[300,200])
# # img.itemset((300,200,0),255)
# # img.itemset((300,200,1),255)
# # img.itemset((300,200,2),255)
# img.itemset((300,200),200)
# img.itemset((200,300),10)
# cv2.imshow("new img",img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.imshow('100_200',cv2.Canny(geet,100,200))
# cv2.imshow('200_400',cv2.Canny(geet,200,400))
# cv2.imshow('200_300',cv2.Canny(geet,200,300))
# cv2.imshow('300_300',cv2.Canny(geet,300,300))

cv2.imshow('geet_blur',cv2.GaussianBlur(geet,(5,5),0))
cv2.imshow('geet',geet)


cv2.waitKey()
cv2.destroyAllWindows()