# Import the pygame module
import pygame
import random
import time
import Ant as a
import Food as f
import Pheremone_Map as pm
import Globals as gl


#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()
ANT_COLOR = g.get_ant_color()
HIVE_COLOR = g.get_hive_color()
MAP_COLOR = g.get_map_color()
FOOD_COLOR = g.get_food_color()


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

# Create the screen object
screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))

#initiate map object
pheremone_map = pm.Pheremone_Map()

#initiate food object
food_locations = f.Food()

#initiate ants stored as a dictionary
ants = {}
for x in range(NUMBER_OF_ANTS):
    ants["ant{0}".format(x)] = a.Ant()
ANTS = pygame.sprite.Group()

#add ants to sprite group
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
        
#         if event.type == pygame.MOUSEBUTTONUP:
#             x,y = pygame.mouse.get_pos()
#             food_locations.add_location([x,y])
              
        # Get all the keys currently pressed
#         pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
        #ant.update(pressed_keys)
        for a in ANTS:
            #a.Pathing()
            a.random_pathing()
            a.check_for_food()
#             a.update(pressed_keys)
#             a.add_location()

        # Fill the screen with map color
        screen.fill(MAP_COLOR)

        for a in ANTS:
            screen.blit(a.surf, a.rect)
            
        for f in FOOD_LOCATIONS:
            x = f[0]
            y = f[1]
            pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(x,y, 20, 20))
                                     
        for h in HIVE_LOCATIONS:
            x = h[0]
            y = h[1]
            pygame.draw.rect(screen, HIVE_COLOR, pygame.Rect(x,y, 20, 20))
            
    elif state == PAUSE:
        
         # Fill the screen with map color
        screen.fill(MAP_COLOR)

        for a in ANTS:
            screen.blit(a.surf, a.rect)
            
        for f in FOOD_LOCATIONS:
            x = f[0]
            y = f[1]
            pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(x,y, 20, 20))
            
        for h in HIVE_LOCATIONS:
            x = h[0]
            y = h[1]
            pygame.draw.rect(screen, HIVE_COLOR, pygame.Rect(x,y, 20, 20))
    
    # Update the display
    pygame.display.flip()
    
#     if(loop_count == 100):
#         print(pheremone_map.get_map())
            
    loop_count += 1
    #time.sleep(.5)

    