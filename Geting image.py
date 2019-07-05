import cv2

img =cv2.imread('adnan.jpg', 0)
print(img)

cv2.imshow('image',img)
k = cv2.waitKey()
if k == 30:
 cv2.destroyAllWindows()

elif k == ord('s'):
 cv2.imwrite("adnan_copy.jpg", 1)
 cv2.destroyAllWindows()