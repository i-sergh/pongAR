import cv2
import numpy as np
from random import randint
import ball


cap = cv2.VideoCapture(0)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

SHOW_CONTOURS = True

cap.set(3,WINDOW_WIDTH) # Установление длины окна
cap.set(4,WINDOW_HEIGHT )  # Ширина окна

#tr, frame = cap.read()
#print(frame.shape)
cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3 ), dtype=np.uint8() )
mrB =[
    ball.Ball(cnv, 320+ randint(0,100), 240+ randint(0,100), 25, (0,255,255))
for i in range(10)]

def findContour (mask, out):
    cont, h = cv2.findContours( mask, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted( cont,key=cv2.contourArea, reverse=True)
    cv2.drawContours( out, cont, 0, (0,255,0), 2 )

    # проверка на пустой список контуров
    if len(cont) == 0:
        return []
    
    for count, i in enumerate(cont[0]):
        
            
        if count % 1 == 0:
            cv2.line(out, (i[0][0], i[0][1]),
                          (cont[0][len(cont[0]) - count - 1][0][0],
                           cont[0][len(cont[0]) - count - 1][0][1]),
                    (randint(0,255), randint(0,255), randint(0,255)), 2)
            
        out[i[0][1], i[0][0], 1] = 255
    return cont[0]
    
       
    

    
while True:
    cnv *=0
    conts = []
    conts1 = []
    tr, frame = cap.read()
    frame = cv2.flip(frame, 2)
    frame_ = cv2.blur( frame, (30, 30) )
    frame_HSV = cv2.cvtColor( frame_,
                              cv2.COLOR_BGR2HSV )

    if SHOW_CONTOURS:
        clr_low, clr_high = ( 0, 100 ,80), (15, 255, 255)
        clr_low1, clr_high1=( 30, 130 ,0), (110, 255, 255)

        frame_clr = cv2.inRange( frame_HSV,clr_low,clr_high)
        conts = findContour (frame_clr, frame)

        frame_clr1 = cv2.inRange( frame_HSV,clr_low1,clr_high1)
        conts1 = findContour (frame_clr1, frame)
  

    for b in mrB:    
        b.move( [[conts], [conts1]])
    
    
    #cv2.imshow('balls', cnv)
    # склейка слоев с мячем и с кадром
    frame = np.where( cnv[:,:]>np.array((0,0,0), dtype=np.uint8()),
                      cnv, frame)
    
    cv2.imshow('mask', frame_clr)    
    cv2.imshow('main', frame )
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    if key == 32:
        
        for b in mrB:
            b.random_restart( 320+ randint(0,100), 240+ randint(0,100), 25 )

    if key == ord('q'):
        SHOW_CONTOURS = not SHOW_CONTOURS
    if key == ord('w'):
        for b in mrB:
            b.giveVelocity(2, 0)
    if key == ord('s'):
        for b in mrB:
            b.giveVelocity(-2, 0)
    if key == ord('a'):
        for b in mrB:
            b.giveVelocity(0, -2)
    if key == ord('d'):
        for b in mrB:
            b.giveVelocity(0, 2)

cv2.destroyAllWindows()
cap.release()
