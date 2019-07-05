import numpy as np
import cv2

#img=cv2.imread('ad.jpg',1)
img=np.zeros([512,520,3], np.uint8)

img= cv2.line(img, (0,0), (230,300), (147,96,50),10)   #44,96 ,147
img= cv2.arrowedLine(img, (0,300), (230,300), (147,0,0),10)
img=cv2.rectangle(img,(384,0), (500,128), (0,0,255),5)
img=cv2.circle(img, (447,63), 63, (0,255,0), -1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img, 'Adnan', (100,600), font, 2, (255,0,0), 10, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()