import sys
import pygame

pygame.init()
screen=pygame.display.set_mode((1000,1000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        sys.exit(0)
    elif event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
        sys.exit(0)