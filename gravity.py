import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((1000,1000))
delta=0.0
FPS=500.0
clock = pygame.time.Clock()
count=500

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
        self.ball=pygame.Rect(x,2,2,2)
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
#Initialize object
obj1=[obj()]
for i in range(count):
    obj1.append(obj())
for i in range(len(obj1)):
    obj1[i].Set_param(1,i*1.5,0,0.92)
    obj1[i].Set_ball(i*2)
while True:   
#Ticking
    pos=list(pygame.mouse.get_pos())
    delta+=clock.tick()/1000.0 
#Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif pygame.mouse.get_pressed()[0]:                       
            for i in range(len(obj1)):
                if obj1[i].Is_inside(pos):
                    obj1[i].Moving_Object()
                else:
                    pass
    while delta > 1/FPS:
        delta-=1/FPS
        screen.fill((0,0,0))       
        if not(pygame.mouse.get_pressed()[0]):     
           for i in range(len(obj1)):
               obj1[i].Update()
        for i in range(len(obj1)):
            pygame.draw.rect(screen,(0,155,155),obj1[i].ball)                
    pygame.display.flip()
        
        
        