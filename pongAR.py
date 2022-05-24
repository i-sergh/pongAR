import cv2
from random import randint
import ball


cap = cv2.VideoCapture(0)

cap.set(3,1920) # Установление длины окна
cap.set(4,1080)  # Ширина окна



mrB = ball.Ball(320+ randint(0,100), 240+ randint(0,100), 50, (0,255,255))


def findContour (mask, out):
    cont, h = cv2.findContours( mask, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted( cont,key=cv2.contourArea, reverse=True)
    cv2.drawContours( out, cont, 0, (0,255,0), 2 )
   
    
    try:
        for count, i in enumerate(cont[0]):
        #print(i[0][0])
            
            if count % 1 == 0:
                cv2.line(out, (i[0][0], i[0][1]),
                          (cont[0][len(cont[0]) - count - 1][0][0],
                           cont[0][len(cont[0]) - count - 1][0][1]),
                    (randint(0,255), randint(0,255), randint(0,255)), 2)
            
            out[i[0][1], i[0][0], 1] = 255
        return cont[0]
    except:
       return []
       
    

    
while True:
    
    tr, frame = cap.read()
    frame = cv2.flip(frame, 2)
    frame_ = cv2.blur( frame, (30, 30) )
    frame_HSV = cv2.cvtColor( frame_,
                              cv2.COLOR_BGR2HSV )

    clr_low = ( 0, 100 ,80)
    clr_high = (15, 255, 255)

    frame_clr = cv2.inRange( frame_HSV,clr_low,clr_high)
    conts = findContour (frame_clr, frame)

    
  

        
    mrB.move(frame, [conts])
    
    

    
    cv2.imshow('mask', frame_clr)    
    cv2.imshow('main', frame )
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    if key == ord('w'):
        mrB.giveVelocity(2, 0)
    if key == ord('s'):
        mrB.giveVelocity(-2, 0)
    if key == ord('a'):
        mrB.giveVelocity(0, -2)
    if key == ord('d'):
        mrB.giveVelocity(0, 2)

cv2.destroyAllWindows()
cap.release()
