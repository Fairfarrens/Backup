import cv2
image1=cv2.imread(r"C:\Users\Fairfarren\Desktop\pearl.jpg")
cv2.imshow("BGR_image",image1)
#BGR色彩空间转RGB色彩空间
image2=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
#RGB色彩空间转HSV色彩空间
image2=cv2.cvtColor(image2,cv2.COLOR_RGB2HSV)
cv2.imshow("HSV_image",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()