import numpy as np
import cv2

# img=np.zeros((1000,1000),dtype=np.uint8)
# # print(img)
# cv2.imshow("new image",img)
# cv2.waitKey(0)
# cv2.destroyWindow()

# def create_img():
#     img = np.zeros([400,400,3],np.uint8)    #创建一个三维数组高400，宽400，信号通道3个，初始都为0，每通道占8位个
#     img[:,:,2] = np.ones([400,400])*255     #将0号通道下[400,400]面积使用ones设置为1，之后乘以255，将其设置为255，注意：3个信道分别是b,g,r所以这里显示为蓝色
#
#     cv2.imshow("your daddy",img)
#
# create_img()
# cv2.waitKey(0)   #等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
# cv2.destroyAllWindows()  #销毁所有窗口

img=np.zeros((200,200,3),dtype=np.uint8)
img[50:150,50:150,2]=200
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()