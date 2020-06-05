import pygame
import pygame.freetype
import math


def InvalidMessage(situation):
    print("==================================================")
    print("Invalid Command!")
    if(situation != 0):
         print("Please issue a command by the following structure:")
    else:
        print("Please issue a Valid Command.")
    if (situation == 1):
         print("<set/add> <variable> <quantity>")
    elif(situation == 2):
        print("<addforce> <x> <y>")


def Draw (velocity, angle, gravity, initX, initY, drawn):
    inAir = 0.0  
    while(drawn == False):
        velocityX = velocity*(math.cos(math.radians(angle)))
        velocityY = velocity*(math.sin(math.radians(angle)))
        inAir = inAir + 0.001

        posX = initX + (velocityX * inAir)
        posY = initY - (velocityY * inAir) - ((1/2)*gravity*inAir**2)
        pygame.draw.circle(screen, WHITE, (int(posX), int(posY)),int(0.5))

        if(posY >= 350):
            drawn = True
    pygame.display.flip()


# Initialize pygame
pygame.init()
BLACK = (0 , 0, 0)
WHITE = (255, 255, 255)

# Window and display surface
screen = pygame.display.set_mode((640,360))
screen.fill(BLACK)
pygame.draw.line(screen, WHITE, (10, 5),(10, 350,), 1)
pygame.draw.line(screen, WHITE, (10, 350),(630, 350,), 1)

# Variables
drawn = False
velocity = 30
gravity = -9.8
angle = 45
initX = 10
initY = 350
viscosity = 1
arrayX = []
arrayY = []

pygame.display.flip()


while(True):

    for event in pygame.event.get():
        #Leave the aplication
        if(event.type == pygame.QUIT):
            exit()

    #Console Message
    print("==================================================")
    print("Firing at " + str(angle) + " degrees, at " + str(int(velocity)) + " m/s.")
    print("Viscosity is " + str(viscosity) + ", gravity is " + str(gravity) + ".")
    print("==================================================")


    #Print the trajectory
    Draw(velocity, angle, gravity, initX, initY, drawn)

    user_input = input().split(' ')

    if(user_input[0] == "set"):
        if(user_input[1] == "velocity"):
            velocity = float(user_input[2])
        elif(user_input[1] == "angle"):
            angle = float(user_input[2]) 
        elif(user_input[1] == "gravity"):
            gravity = -float(user_input[2]) 
        elif(user_input[1] == "viscosity"):
            viscosity = float(user_input[2])
        else:
            InvalidMessage(1)
            
    elif(user_input[0] == "addforce"):
        if(len(user_input) == 3):
            arrayX.append(float(user_input[1]))
            arrayY.append(float(user_input[2]))
        else:
            InvalidMessage(2)

    elif(user_input[0] == "forces"):
        for i in range(len(arrayX)):
            print(str(i) + ". F = (" + str(arrayX[i]) + " " + str(arrayY[i]))

    elif(user_input[0] == "removeforce"):
        arrayX.pop(int(user_input[1]))
        arrayY.pop(int(user_input[1]))

    else:
        InvalidMessage(0)
        
    #Fill Black then #pygame.draw.line(screen, WHITE, (10, 5),(10, 350,), 1) #pygame.draw.line(screen, WHITE, (10, 350),(630, 350,), 1)


 