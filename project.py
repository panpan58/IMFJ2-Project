import pygame
import pygame.freetype


# Initialize pygame
pygame.init()

# Window and display surface
screen = pygame.display.set_mode((640,360))

while(True):
    for event in pygame.event.get():
            #para sair da aplicação
            if(event.type == pygame.QUIT):
                exit()