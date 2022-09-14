import cv2
from random import randint
import ball
import numpy as np



img = cv2.imread('test_res\\imgfig.jpg')

                       
img_mask = np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8() )

img_mask = np.where(img == (0,255,0), 255, 0)
img_mask = np.uint8(img_mask)

      
cv2.imshow('img', img)

cv2.imshow('mask img', img_mask)

cv2.waitKey(0)

cv2.destroyAllWindows()
