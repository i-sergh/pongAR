import cv2
import numpy as np
from random import randint

## TODO
'''
 переписать физику ,привязав движение к векторным вычислениям
 a^2 + b^2 - 2a*b*cos(alpha)

Движение происходит через сумму векторов X Y, соответственно, угол между нмими всегда 90 град
cos(90) = 0

значит, используем
a^2 + b^2

Не используем, для расширения нужно сталкивать вектор движения с другим
'''



class Ball:
    def __init__ (self, cnv, x, y, r, clr):
        self.cnv = cnv
        self.x = x
        self.y = y
        self.r = r
        self.clr = clr
        self.vx = randint(-20,20)
        self.vy = randint(-20,20)
        self.MAX_VELOCITY = 50
        if self.vx > 0:
            self.vecX = 1
        else:
            self.vecX = -1

        if self.vy > 0:
            self.vecY = 1
        else:
            self.vecY = -1
            
        self.back_clr = (0,0,0)
    
        
    def draw(self):
        cv2.circle( self.cnv, (self.x,self.y), self.r, self.clr, -1 )

        self.draw_vec() 
        

    def draw_vec(self):
        cv2.circle( self.cnv,
                    ( self.x + self.vx + self.r *  self.vecX,
                      self.y + self.vy + self.r *  self.vecY ),
                    3, (0,0,255), -1 )

        
        
            
    def destroy(self): 
        cv2.circle( self.cnv, (self.x,self.y), self.r, self.back_clr, -1 )

    def bounceX (self):
        self.vx *= -1
        self.vecX *= -1
    def bounceY(self):
        self.vy *= -1
        self.vecY *= -1

    def next_step_check (self):
        # X-es

        # right border
        if self.x + self.vx + self.r  > self.cnv.shape[1]:
            self.bounceX()
            
            if abs(self.vx) > 2:
               self.vx  = int(self.vx*0.9)
               
        # left border
        if self.x + self.vx - self.r  < 0:
            self.bounceX()
            if abs(self.vx) > 2:
               self.vx  = int(self.vx*0.9)

        # Y-es
        
        #  down border
        if self.y + self.vy + self.r  > self.cnv.shape[0]:
            self.bounceY()
            if abs(self.vy) > 2:
               self.vy  = int(self.vy*0.9)
        # upper border
        if self.y + self.vy - self.r  < 0:
            self.bounceY()
            if abs(self.vy) > 2:
               self.vy  = int(self.vy*0.9)

               
    def collision_contour_check(self, conts):
        """
            collisionContourCheck - проверяет коллизию контуров конкретного цвета
            Если объект касается контура, то объект отскакивает

            conts: [[]] - список контуров cv2 конкретного (одного) цвета
            
        """
        # проверка на пустой список контуров
        if len(conts[0]) == 0:
            return 0
            
                    
        if cv2.pointPolygonTest(conts[0], # контур
                                ( self.x + self.vx + self.r *  self.vecX,  #  следующий шаг  X
                                 self.y + self.vy + self.r *  self.vecY ),#                 Y
                                True) >= 0: # если в контуре, то происходит отскок                  
                #if randint(0,1):
            self.bounceX ()
                #else:
            self.bounceY ()
            if abs(self.vx) <= self.MAX_VELOCITY:
                self.vx  = int(self.vx*2)
            else:
                self.vx = self.MAX_VELOCITY
                        
            if abs(self.vy) <= self.MAX_VELOCITY:
                self.vy  = int(self.vy*2)
            else:
                self.vy = self.MAX_VELOCITY
        
    def move(self, conts=[] ):
        """
            move - двигает объект на шаг, равный dx, dy

            conts: [ [[]], [[]] ] - список контуров cv2 различных цветов; conts[i] - список контуров конкретного цвета
        """
        self.destroy()

        self.next_step_check()
        # в conts список из 
        for cont in conts:    
            self.collision_contour_check(cont)
        # Dx Dy
        self.x += self.vx
        self.y += self.vy

        self.draw()
        
    def give_velocity(self, vx, vy):
        self.vx += vx
        self.vy += vy

    def set_X(self, X):
        self.x = X
        
    def set_Y(self, Y):
        self.y = Y
        
    def set_R(self, R):
        self.r = R
        
    def set_color(self, color):
        self.clr = color

    def set_max_velocity(self, max_velocity):
        self.MAX_VELOCITY = max_velocity
        
    def set_velocity(self,vx=None, vy=None):
        if vx == None:
            self.vx = randint(-20,20)
        if vy == None:
            self.vy = randint(-20,20)
        
        if self.vx > 0:
            self.vecX = 1
        else:
            self.vecX = -1

        if self.vy > 0:
            self.vecY = 1
        else:
            self.vecY = -1

    def set_color(self, color):
        if color == None:
            self.clr = (randint(0,255), randint(0,255), randint(0,255))
        else:
            self.clr = color
    
    def random_restart (self, X=None, Y=None, R=None, color=None, vx=None, vy=None ):
        # TODO: Отрефакторить
        if not R:
            self.r = randint(10, 75)
        else:
            self.r = R
            
        if X == None:
            self.x = randint(0 + self.r, self.cnv.shape[1] - self.r)
        else:
            self.x = X
            
        if Y == None:
            self.y = randint(0 + self.r, self.cnv.shape[0] - self.r)
        else:
            self.y = Y
            
        self.set_color(color)
        
        self.set_velocity(vx, vy)  
            
if __name__ == '__main__':
    cnv = np.ones( (600, 600, 3), dtype=np.uint8() )

    ball = Ball( 300+ randint(0,100), 300+ randint(0,100), 50, (0,255,255))

    while True:

        ball.move(cnv)
        cv2.imshow('main', cnv)
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        if key == ord('w'):
            ball.give_velocity(2, 0)
        if key == ord('s'):
            ball.give_velocity(-2, 0)
        if key == ord('a'):
            ball.give_velocity(0, -2)
        if key == ord('d'):
            ball.give_velocity(0, 2)
    
    cv2.destroyAllWindows()
