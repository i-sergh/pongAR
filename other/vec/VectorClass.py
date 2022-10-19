import cv2

import numpy as np

def grad2deg(deg):
    return deg *np.pi/180

  

class Vector:
    def __init__ (self, cnv, pos, leng, ang, color):
        self.cnv = cnv
        self.x = pos[0]
        self.y = pos[1]

        self.leng = leng

        self.color = color

        self.dang = grad2deg(np.random.random()+ ( -1)*np.random.randint(0, 1))/0.1
        self.ang = grad2deg(ang)
        self.aim = False
    
    def draw (self):
        cv2.line( self.cnv, (self.x, self.y),
                  (self.x + int(self.leng*np.sin(self.ang)),
                   self.y+ int(self.leng*np.cos(self.ang))),
                self.color, 1)
        
    def destroy (self):
        cv2.line( self.cnv, (self.x, self.y),
                  (self.x + int(self.leng*np.sin(self.ang)),
                   self.y+ int(self.leng*np.cos(self.ang))),
                (0,0,0), 1)

    def reset_dang(self):
        self.dang = grad2deg(np.random.random()+ ( -1)*np.random.randint(0, 1))/0.1

    def set_target(self, target):
        self.target = grad2deg(target)
        self.aim = True
        
    def target_missed(self):
        if self.target > self.ang:
            if self.dang > 0:
                return True
            else:
                self.dang = self.dang/(-2)
                return True
        elif self.target < self.ang:
            if self.dang < 0:
                return True
            else:
                self.dang = self.dang/(-2)
                return True
        return False
    
    def rotate(self):
        if  self.aim  and self.target_missed():
            self.destroy()
            self.ang += self.dang
            #print(self.target, self.ang, self.dang)
            if self.ang < 0:
                self.ang = 360 + self.ang
            if self.ang > 360:
                self.ang = self.ang - 360
        
            self.draw()
        else:
            self.aim = False
            self.reset_dang()

if __name__ == '__main__':
    def draw_circle (event, x, y, flags, param): # Пропущенные параметры: событие мыши, координаты, где произошло событие мыши, FLAG
        if event==cv2.EVENT_LBUTTONDOWN:
            for vec in vecs:
                vec.set_target(np.random.randint(0,360))
                vec.target_missed()
    cnv = np.zeros( (600,600,3), dtype=np.uint8() )
        
    cv2.namedWindow('canvas')
    cv2.setMouseCallback('canvas',draw_circle)
    vecs = []
    #i,j = 300, 300
    #vecs += [Vector(cnv, (i,j), 60,
    #                        np.random.randint(0,360),
    #                        (int((i/600)*255), int((j/600)*255), 200))]
    #vecs[-1].draw()
    #'''
    for i in range(0,600, 6):
        for j in range(0, 600, 6):
            vecs += [Vector(cnv, (i,j), 6,
                            np.random.randint(0,360),
                            (int((i/600)*255), int((j/600)*255), 200))]
            vecs[-1].draw()
    #'''        
    while True:
        cv2.imshow('canvas', cnv)
        key = cv2.waitKey(1)
        for vec in vecs:
            vec.rotate()

        if key == 27: #ESC
            break
    cv2.destroyAllWindows()
