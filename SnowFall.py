import pygame
import random

#initialize pygame

pygame.init()

#declaration of some colours

BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE =[0,0,255]
YELLOW = [255,255,0]
PINK = [255,15,192]

#size of the screen
SIZE  = [1240,720]

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Snow Animation")

#lists of snowflakes and their sizes
snow_list = []
size_list = []

#creating a list of 300 snowflakes with sizes ranging from 1 px to 2 px

for i in range(300):
    x = random.randrange(0,1240)
    y = random.randrange(-720,-1)
    snow_list.append([x,y])
    size_list.append(random.randrange(1,3))

#creating a list of 10 snowflakes with sizes ranging from 4 px to 5 px

for i in range(10):
    x = random.randrange(-720,0)
    y = random.randrange(-7200,-1)
    snow_list.append([x,y])
    size_list.append(random.randrange(4,6))

#a clock object   
clock = pygame.time.Clock()

done  = False

while not done:

    #when the screen is closed this is executed
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done  = True

    #the screen background is set to black
            
    screen.fill(BLACK)

    #iterating over all the snowflakes
    
    for i in range(len(snow_list)):     

       #draw a white circle on the screen with locations as specified by the
       #snowflake's x and y values and set its size to the random value assigned
        
       pygame.draw.circle(screen, WHITE, snow_list[i], size_list[i])

       #definition of the speed at which the snowflake falls down
       
       speed = 2*size_list[i]
       snow_list[i][1]+= speed

       #when the snowflake reaches the bottom of the screen, reset its position
       #to a random value
       
       if snow_list[i][1]>720:
            y=random.randrange(-500,-5)
            snow_list[i][1] = y
            x= random.randrange(-200,1240)
            snow_list[i][0] = x

    #display
    
    pygame.display.flip()
    clock.tick(20)

#quits smoothly on closing the screen. 
pygame.quit()
