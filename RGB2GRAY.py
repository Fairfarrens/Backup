import cv2

image1=cv2.imread(r"C:\Users\Fairfarren\Desktop\pearl.jpg")
cv2.imshow("Origin",image1)
#RGB色彩空间转GRAY色彩空间
image2=cv2.cvtColor(image1,cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
