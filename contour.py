import cv2
from random import randint
import ball
import numpy as np



img = cv2.imread('test_res\\imgfig.jpg')

print(type(img))                       
img_mask = np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8() )

img_mask[img[:,:,0] > 200] = 255

cont, h = cv2.findContours(img_mask,
                           cv2.RETR_TREE,
                           cv2.CHAIN_APPROX_SIMPLE)

cont = (cont[0],
        np.array(
            [
                [[100, 100]],
                [[100, 200]],
                [[200, 200]],
                
                [[200, 100]],

                [[ 190, 110]]
                ]
                    )
        )
print(len(cont[0]))
print(cont[0])   
cv2.imshow('img', img)

cv2.imshow('mask img', img_mask)
cv2.drawContours( img, cont, -1, (0,255,255), 2 )
for i in range(len(cont[0])):
    cv2.circle(img, (cont[0][i][0][0],cont[0][i][0][1]),2, (0,0,255), -1 )
cv2.imshow('imgcont', img)


cv2.waitKey(0)

cv2.destroyAllWindows()
