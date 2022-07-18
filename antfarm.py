# Import the pygame module
import pygame
import random
import time
import Ant as a
#import Food as f
import Pheremone_Map as pm
import Globals as gl
import Functions
import numpy as np
import Variables

fun = Functions.Functions()
v = Variables.Variables()
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
HIVE_SIZE = g.get_hive_size()
FOOD_SIZE = g.get_food_size()

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
p = pm.Pheremone_Map()

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
        pressed_keys = pygame.key.get_pressed()

        #ANT INSTRUCTIONS EACH LOOP
        for a in ANTS:
            
            a.Pathing()
            a.update(pressed_keys)

        # Fill the screen with map color
        
        screen.fill(MAP_COLOR)

#VIEW ANT SMELL RADIUS
#         for l in (fun.surrounding_squares(a.ant_location())):
#             pygame.draw.rect(screen,(255,40,255), pygame.Rect(l[0],l[1], 1, 1)) #shows the ant smell radius

            
# VIEW FOOD PHEREMONE TRAILS
#         food_pheremone_map = p.get_food_pheremone_map()
#         
#         count = 0
#         for y in range(MAP_HEIGHT - 1):
#          for x in range(MAP_WIDTH - 1):
#             if (food_pheremone_map[x][y] > 0):
#                 pygame.draw.rect(screen,(255,40,255), pygame.Rect(x,y, 1, 1))
        
#VIEW HOME PHEREMONE TRAILS           
#         home_pheremone_map = p.get_home_pheremone_map()
# 
# 
#         count = 0
#         for y in range(MAP_HEIGHT - 1):
#             for x in range(MAP_WIDTH - 1):
#                 if (home_pheremone_map[x][y] > 0):
#                     pygame.draw.rect(screen,(255,255-(home_pheremone_map[x][y] * 10),255), pygame.Rect(x,y, 1, 1))

#         food_pheremone_map = p.get_food_pheremone_map()
        
#VIEW THE MAX AND MIN VALUES OF THE PHEREMONE MAPS

#         food_map = p.get_food_pheremone_map()
#         print("Food map max: " + str(np.max(food_map)))
#         print("Food map min: " + str(np.min(food_map)))
#         home_map = p.get_home_pheremone_map()
#         print("Home map max: " + str(np.max(home_map)))
#         print("Home map min: " + str(np.min(home_map)))
        
        
#VIEW THE AMOUNT OF TOTAL FOOD DEPOSITED
#         print(v.get_total_food_collected())

        for a in ANTS:
            screen.blit(a.surf, a.rect)
            
        for f in FOOD_LOCATIONS:
            x = f[0]
            y = f[1]
            pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(x,y, FOOD_SIZE, FOOD_SIZE))
                                     
        for h in HIVE_LOCATIONS:
            x = h[0]
            y = h[1]
            pygame.draw.rect(screen, HIVE_COLOR, pygame.Rect(x,y, HIVE_SIZE, HIVE_SIZE))
                
    elif state == PAUSE:
        
         # Fill the screen with map color
        screen.fill(MAP_COLOR)

        for a in ANTS:
            screen.blit(a.surf, a.rect)
            
        for f in FOOD_LOCATIONS:
            x = f[0]
            y = f[1]
            pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(x,y, FOOD_SIZE, FOOD_SIZE))
                                     
        for h in HIVE_LOCATIONS:
            x = h[0]
            y = h[1]
            pygame.draw.rect(screen, HIVE_COLOR, pygame.Rect(x,y, HIVE_SIZE, HIVE_SIZE))
        
    #pheremone decay
    p.pheremone_decay()
    # Update the display
    pygame.display.flip()
    loop_count += 1
    #time.sleep(.5)

    