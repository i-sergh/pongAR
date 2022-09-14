import cv2
from random import randint
import ball
import numpy as np



img = np.zeros((480, 640, 3), dtype=np.uint8() )

cv2.circle(img, (320, 240), 50, (0,255,0), -1 )

cv2.rectangle(img, (50, 50), (100, 100), (255,0,0), -1 )

cv2.imshow('img Circle', img)
cv2.imwrite('test_res\\imgfig.jpg', img)


cv2.waitKey(0)

cv2.destroyAllWindows()
