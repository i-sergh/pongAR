import cv2
import numpy as np
from random import randint
from ball import Ball


class Player:

    def __init__(self, color, cnv):
        self.color = color
        self.cnv = cnv 
        #self.player_side = player_side # а нужно ли оно именно сдесь
        self.test = False
        
    def findMyself(self):
        pass



if __name__ == '__main__':
    cnv = np.ones( (600, 600, 3), dtype=np.uint8() )

    player = Player((0,200,0), cnv)
    
    ball = Ball( 300+ randint(0,100), 300+ randint(0,100), 50, (0,255,255))

    while True:
        cnv *= 0
        
        cv2.imshow('main', cnv)
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        if key == ord('q'):
            player.testDraiw()
        if key == ord('w'):
            ball.giveVelocity(2, 0)
        if key == ord('s'):
            ball.giveVelocity(-2, 0)
        if key == ord('a'):
            ball.giveVelocity(0, -2)
        if key == ord('d'):
            ball.giveVelocity(0, 2)
    
    cv2.destroyAllWindows()    
