import numpy as np
import cv2 as cv
# im = cv.imread('geet.png')
im=cv.imread('3.jpg')
print(im.shape)
img=cv.GaussianBlur(im,(5,5),0)
# imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# ret, thresh_blur = cv.threshold(imgray, 150, 255, 0)
thresh_blur=cv.Canny(img,100,200)
# thresh=cv.Canny(im,200,400)
cv.imshow('thresh_blur',thresh_blur)
# cv.imshow('thresh',thresh)
contours_blur, hierarchy_blur = cv.findContours(thresh_blur, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# cv.imshow('轮廓',cv.drawContours(thresh_blur,contours_blur,-1,255,3))
# M=cv.moments(contours_blur[0])
# print(M)
# print(contours,hierarchy)
# print(type(contours))
# print(len(contours_blur))
# print(contours[0])
# print('去噪后的轮廓',len(contours_blur))
# print('去噪前的轮廓',len(contours))
# a=0

img=np.zeros((390,680))

for contour in contours_blur:
    # print(cv.contourArea(contour))
    # for point in contour:
    #     if cv.contourArea(contour)==55.5:
    #         img.itemset((point[0,1],point[0,0]),255)
    # if contour.shape[0]>50:
    #     print(contour.shape)
    #     print("*"*60)
    # print('这块区域的面积是%d'%cv.contourArea(contour))
    if cv.contourArea(contour)>4000 and cv.contourArea(contour)<8000:
    # if cv.contourArea(contour)>10000:
    # if 30<cv.arcLength(contour,True)<400:
        print("这块区域的面积是%d"%cv.contourArea(contour))
        # print('这块区域的面积是%d'%cv.arcLength(contour,True))
        # print(contour.size)
        for point in contour:
            print(point)
            # print(point[0])
            img.itemset((point[0,1],point[0,0]),255)
    # print('第%d块轮廓的面积是%d'%(contours_blur.index(contour),cv.contourArea(contour)))
    # print("这块轮廓的面积是%d"%cv.contourArea(contour))
        # a+=1
cv.imshow('new img',img)
# print("a的值是%d"%a)
cv.waitKey()
cv.destroyAllWindows()
# print(len(contours))
# print(im.shape,im.size)
# print(np.size(contours))
# print(hierarchy.shape)
# for hierarchy_solo in hierarchy[0]:
#     print(hierarchy_solo)
# print(hierarchy[0])