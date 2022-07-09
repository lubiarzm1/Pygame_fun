import pygame
import sys

pygame.init()
#Klasa pozwala na przemieszczanie obiektow po ekranie
#Metoda check zajmujes sie wyznaczaniem parametru przemiesczania
class BoxUp():
    out=[0,0]
    def __init__(self):
        out=[1.0,1.0] 
    def check(self,y,x,m):
        v=[y,x]
        for i in range(len(v)):
            if v[i] > screen.get_width()-51:
                self.out[i]=-1*m
            elif v[i] < 51:
                self.out[i]=1*m
            else:
                pass
#Tablica z obiektami klasy Kwadrat                    
box=[pygame.Rect(50,50,50,50),pygame.Rect(150,50,50,50),pygame.Rect(250,50,50,50),pygame.Rect(350,50,50,50)]
#Inicjalizacja ekranu
screen=pygame.display.set_mode((1000,1000))
#Klasa z obietkami klasy obliczajacej
boxUP=[BoxUp(),BoxUp(),BoxUp(),BoxUp()]
delta = 0.0
#deklaracja zegara
clock = pygame.time.Clock()
#Wyzwalanie funkcji
while True:
    ##Handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
            sys.exit(0)
    print(pygame.mouse.get_pos())
    screen.fill((0,0,0))
#Ticking
    delta+=clock.tick()/1000.0
        
# INPUTS
    while delta>=(1/60.0):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d]:
            #Wykonywanie polecenia dla wszystkich obietów
            for i in range(4):
                #wywolanie funkcji wektora przemieszczenia
                boxUP[i].check(box[i].y,box[i].x,float(20))
                #inkrementacja pozycji
                box[i].x+=boxUP[i].out[1]
        if keys[pygame.K_s]:
            for i in range(4):
                boxUP[i].check(box[i].y,box[i].x,float(20))
                box[i].y+=boxUP[i].out[0]
        for i in range(len(box)):
            pygame.draw.rect(screen,(0,155,155),box[i])
        pygame.display.flip()
        delta-=(1/60.0)