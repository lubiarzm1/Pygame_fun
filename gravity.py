import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((1000,1000))
ball=pygame.Rect(475,50,50,50)
delta=0.0
clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
#Ticking
    delta+=clock.tick()/1000.0
#Position conversion
    pos=list(pygame.mouse.get_pos())
#Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    if pygame.mouse.get_pressed() and pos[0]>ball.x-25 and pos[0]<ball.x+25 and pos[1]>ball.y-25 and pos[1]<ball.y+25 :           
        ball.x=pos[0]
        ball.y=pos[1]
        h_start=screen.get_height()-(ball.y+50)
    while delta<1/60.0:
        delta-=1/60.0
        if not(pygame.mouse.get_pressed() and pos[0]>ball.x-25 and pos[0]<ball.x+25 and pos[1]>ball.y-25 and pos[1]<ball.y+25) and ball.y<950:
            ball.y+=1
        pygame.draw.rect(screen,(0,155,155),ball)
    pygame.display.flip()
        