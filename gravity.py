import pygame
import sys
from class_obj import obj

pygame.init()
screen=pygame.display.set_mode((1000,1000))
delta=0.0
FPS=500.0
clock = pygame.time.Clock()
count=500

#Initialize object
obj1=[obj()]
for i in range(count):
    obj1.append(obj())
for i in range(len(obj1)):
    obj1[i].Set_param(1,i*1.5,0,0.85)
    obj1[i].Set_ball(i*2)      
##MAIN    
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
        
        
        