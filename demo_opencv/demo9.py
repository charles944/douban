import numpy as np
import cv2

img=np.zeros((400,400,3),np.uint8)
# img[100:300,100:300]=(0,0,255)
img[50:150,50:150]=(0,0,255)
img[50:150,250:350]=(0,0,255)
img[250:350,50:150]=(0,0,255)
img[250:350,250:350]=(0,0,255)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(cv2.Canny(img_gray,200,400), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
print(hierarchy)
# for contour in contours:
#     print('这个轮廓的面积是%d'%cv2.contourArea(contour))
#     print(contour.size)
#     print(contour.shape)
    # print(contour)
# for hierarchy_loso in hierarchy:
    # print(hierarchy_loso)



cv2.imshow('img',cv2.Canny(img_gray,200,400))
cv2.waitKey()
cv2.destroyAllWindows()