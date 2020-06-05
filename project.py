import pygame
import pygame.freetype
import math
import random
import time


# Initialize pygame
pygame.init()
BLACK = (0 , 0, 0)
WHITE = (255, 255, 255)

# Window and display surface
screen = pygame.display.set_mode((640,360))
screen.fill(BLACK)
pygame.draw.line(screen, WHITE, (10, 5),(10, 350,), 1)
pygame.draw.line(screen, WHITE, (10, 350),(630, 350,), 1)

#Valores default da parabola 
drawed = False
velocity = 30
gravity = -9.8
angle = 45
initX = 10
initY = 350
velocityX = velocity*(math.cos(math.radians(angle)))
velocityY = velocity*(math.sin(math.radians(angle)))

pygame.display.flip()
while(True):

    for event in pygame.event.get():
        #para sair da aplicação
        if(event.type == pygame.QUIT):
            exit()

    

    #Dá print da parabola
    inAir = 0.0
    while(drawed == False):

        inAir = inAir + 0.01

        posX = initX + (velocityX * inAir)
        posY = initY - (velocityY * inAir) - ((1/2)*gravity*inAir**2)
        pygame.draw.circle(screen, WHITE, (int(posX), int(posY)),int(0.5))

        if(posY >= 350):
            drawed = True

    pygame.display.flip()
 