from tkinter import Y
import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,1000))
ball=pygame.Rect(475,50,50,50)
delta=0.0
t=0.0
g=9.81
a=0.0
h_start=0.0
m=1


clock = pygame.time.Clock()
drop_time = pygame.time.Clock()

Epot=0.0
Ekin=0.0
Eroz=0.0

while True:   
#Ticking
    pos=list(pygame.mouse.get_pos())
    mouse_inside= pos[0]>ball.x and pos[0]<ball.x+50 and pos[1]>ball.y and pos[1]<ball.y+50
    delta+=clock.tick()/1000.0
    t+=drop_time.tick()/1000.0
 
#Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif pygame.mouse.get_pressed()[0] and mouse_inside:           
            ball.x=pos[0]-25
            ball.y=pos[1]-25
            t=0.0
            h_start=(ball.y)
               
                    
    while delta >= 1/120:
        delta-=1/120
        screen.fill((0,0,0))
        if not(pygame.mouse.get_pressed()[0]) and ball.y<950:          
            ball.y=h_start+(g/2)*t**2
        pygame.draw.rect(screen,(0,155,155),ball)
    pygame.display.flip()
        
        
        