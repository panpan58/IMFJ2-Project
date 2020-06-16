import pygame
import pygame.freetype
import math


def Messages(situation):
    
    print("==================================================")
    if(situation == 0):
        print("Please issue a Valid Command.") 
    elif(situation == 1 or situation == 2):
        print("Please issue a command by the following structure:")

    if (situation == 1 or situation == 5):
        if(situation == 5): 
            print("To change the paramaters of the trajectory:")
        print("'set <variable> <quantity>'")

    if(situation == 2 or situation == 5):
        if (situation == 5): 
            print("To add an external Force to the trajectory:")
        print("'addforce <x> <y>'")

    if (situation == 5):
        print("To see a list of current External Forces Type 'forces'")
        print("To remove an external force type 'removeforce <force list position>'")
        print("To leave the application type 'exit'.")
    
    else: 
        print("Or type 'help' for the list of commands.")


def Draw (velocity, angle, gravity, initX, initY, drawn, arrayX, arrayY, mass, viscosity):
    inAir = 0.0  
    BLACK = (0 , 0, 0)
    WHITE = (255, 255, 255)

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (10, 5),(10, 350,), 1)
    pygame.draw.line(screen, WHITE, (10, 350),(630, 350,), 1)

    while(drawn == False):

        velocityX = velocity*(math.cos(math.radians(angle)))
        velocityY = velocity*(math.sin(math.radians(angle)))

        for i in range(len(arrayX)):
            velocityX = velocityX + (arrayX[i]/mass)
            velocityY = velocityY + (arrayY[i]/mass)
            
        inAir = inAir + 0.001

        posX = initX + (velocityX * inAir)
        posY = initY - (velocityY * inAir) - ((1/2)*gravity*inAir**2)
        pygame.draw.circle(screen, WHITE, (int(posX), int(posY)),int(0.5))

        if(posY >= 350 or posX >= 640):
            drawn = True
    pygame.display.flip()



# Initialize pygame
pygame.init()


# Window
screen = pygame.display.set_mode((640,360))

# Variables
drawn = False
velocity = 30
gravity = -9.8
angle = 45
initX = 10
initY = 350
viscosity = 1
mass = 1
arrayX = []
arrayY = []

pygame.display.flip()


while(True):

    for event in pygame.event.get():
        #Leave the application
        if(event.type == pygame.QUIT):
            exit()

    #Console Standart Message
    print("==================================================")
    print("Firing at " + str(angle) + " degrees, at " + str(int(velocity)) + " m/s.")
    print("Viscosity is " + str(viscosity) + ", gravity is " + str(gravity) + ".")
    print("==================================================")


    #Print the trajectory
    Draw(velocity, angle, gravity, initX, initY, drawn, arrayX, arrayY, mass, viscosity)

    #Command the user inputs
    original_input = input()
 
    #Leave the aplication
    if(original_input == "exit"):
        exit()


    #Verifies which command the user inputs and if it is correct
    try:
        user_input = original_input.split(' ')
        if(user_input[0] == "set"):
            if(user_input[1] == "velocity"):
                velocity = float(user_input[2])
            elif(user_input[1] == "angle"):
                angle = float(user_input[2]) 
            elif(user_input[1] == "gravity"):
                gravity = -float(user_input[2])
            elif(user_input[1] == "mass"):
                mass = -float(user_input[2]) 
            elif(user_input[1] == "viscosity"):
                viscosity = float(user_input[2])
            else:
                Messages(1)
                
        elif(user_input[0] == "addforce"):
            if(len(user_input) == 3):
                arrayX.append(float(user_input[1]))
                arrayY.append(float(user_input[2]))
            else:
                Messages(2)

        elif(user_input[0] == "forces"):
            if (len(arrayX) != 0):
                for i in range(len(arrayX)):
                    print(str(i) + ". F = (" + str(arrayX[i]) + " " + str(arrayY[i]))
            else: print("There are no external forces being applied!")

        elif(user_input[0] == "removeforce"):
            arrayX.pop(int(user_input[1]))
            arrayY.pop(int(user_input[1]))

        elif(user_input[0] == "help"):
            Messages(5)

        else:
            Messages(0)

    except:
        Messages(0)