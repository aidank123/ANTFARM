# Import the pygame module
import pygame
import random
import time
import Ant as a
import Food as f
import Pheremone_Map as pm

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Initialize pygame
pygame.init()


# Define constants for the screen width and height
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#initiate map

pheremone_map = pm.Pheremone_Map()
# Instantiate ants. Right now, this is just a rectangle.
#initiate food 
food_locations = f.Food()

ants = {}
for x in range(100):
    ants["ant{0}".format(x)] = a.Ant()
ANTS = pygame.sprite.Group()

for a in ants:
    ANTS.add(ants[a])

# Variable to keep the main loop running
RUNNING, PAUSE = 0, 1
state = RUNNING
loop_count = 0

# Main loop
while True:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == pygame.K_p: state = PAUSE
            if event.key == pygame.K_s: state = RUNNING
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    if state == RUNNING:
        
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            food_locations.add_location([x,y])
              
        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
        #ant.update(pressed_keys)
        for a in ANTS:
            a.random_pathing()
            a.update(pressed_keys)
            a.add_location()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        for a in ANTS:
            screen.blit(a.surf, a.rect)
            
        for f in food_locations.get_map():
            x = f[0]
            y = f[1]
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,y, 20, 20))
            
    elif state == PAUSE:
        
         # Fill the screen with black
        screen.fill((0, 0, 0))

        for a in ANTS:
            screen.blit(a.surf, a.rect)
            
    
    # Update the display
    pygame.display.flip()
    
    if(loop_count == 100):
        print(pheremone_map.get_map())
            
    loop_count += 1
    #spacebar to pause game
    