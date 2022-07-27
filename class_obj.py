import pygame
import sys
FPS=60.0
pygame.init()
pos=list(pygame.mouse.get_pos())
class obj():
    ## Init
    def __init__(self):
        self.ball=pygame.Rect(475,50,50,50)
        self.lock_y = False
        self.t=0.0
        self.v=0.0
        self.g=10
        self.last_pos=0
        self.sigma=1
    ## Calculating position iside
    def Is_inside(self,pos):
        return(pos[0]>self.ball.x and pos[0]<self.ball.x+50 and pos[1]>self.ball.y and pos[1]<self.ball.y+50)
    ##Setter of parameters
    def Set_param(self,g,last_pos,v,sigma):
        self.g=g
        self.last_pos=last_pos
        self.v=v
        self.sigma=-sigma
    ##Initialaizing obj
    def Set_ball(self,x):
        self.ball=pygame.Rect(x,10,10,10)
    ##Phisic of ball
    def Update(self):
        self.t+=1/FPS
        if self.ball.y > 950 and self.lock_y == False:
            self.t=0.0
            self.v= self.sigma*self.v
            self.last_pos=950
            self.lock_y = True
        elif self.ball.y < 950 and self.lock_y == True:
            self.lock_y = False
            self.t=0.0
        else:
            self.v=self.v+self.g*self.t
            self.ball.y=self.last_pos+self.v*self.t
            self.last_pos=self.ball.y
    ##Method to moving object
    def Moving_Object(self):
            self.ball.x=pos[0]-25
            self.ball.y=pos[1]-25
            self.last_pos=self.ball.y
            self.t=0.0