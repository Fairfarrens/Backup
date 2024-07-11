import cv2
image1=cv2.imread(r"C:\Users\Fairfarren\Desktop\pearl.jpg",4 )
cv2.imshow("BGR image1",image1)
#RGB色彩空间转YCrCb色彩空间
image2=cv2.cvtColor(image1,cv2.COLOR_RGB2YCrCb)
cv2.imshow("YCrCb image",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()