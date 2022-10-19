import cv2

import numpy as np

def grad2deg(deg):
    return deg *np.pi/180

cnv = np.zeros( (600,600,3), dtype=np.uint8() )


ang = 0
color = (0, 100, 255)
leng = 100
while True:
    #cnv *= 0

    cv2.line(cnv, ( 300, 300),
             (500 + int(leng*np.sin(ang)),500+int(leng*np.cos(ang)) ),
             (0,0,0), 2)
    ang +=0.01
    cv2.line(cnv, ( 300, 300),
             (500 + int(leng*np.sin(ang)),500+int(leng*np.cos(ang)) ),
             (0,255,0), 2)
    cv2.circle(cnv, (500, 500), 100, (255, 0, 0), 2)
    cv2.circle(cnv, (500, 500), 4, (0, 255, 255), -1)
    cv2.circle(cnv, (300, 300), 4, (0, 255, 255), -1)

    cv2.circle(cnv, ( int(leng*np.sin(ang))+300, int(leng*np.sin(ang))+100),
               4, color, -1)
    cv2.circle(cnv,
               (500 + int(leng*np.sin(ang)),500+int(leng*np.cos(ang)) ),
               4, (0, 100, 255), -1)

    
    
    if ang > 360:
        ang = 0
        color = (0, 100, 255)
    if ang > 180:
        color = (180, 100, 0)
    cv2.imshow('canvas', cnv)

    
    
    key = cv2.waitKey(1)

    if key == 27: #ESC
        break

cv2.destroyAllWindows()
