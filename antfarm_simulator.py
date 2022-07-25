#NUMBER OF ITERATIONS TO RUN
NUMBER_OF_ITERATIONS = 1000

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
p = pm.Pheremone_Map()

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

#initiate ants stored as a dictionary
ants = {}
for x in range(NUMBER_OF_ANTS):
    ants["ant{0}".format(x)] = a.Ant()
ANTS = pygame.sprite.Group()

#add ants to sprite group
for a in ants:
    ANTS.add(ants[a])

#runs a simulation for the specified number of iterations before displaying the results
loop_count = 0
while loop_count < NUMBER_OF_ITERATIONS:
    for a in ANTS:            
        a.Pathing()
    #pheremone decay
    p.pheremone_decay()
    loop_count += 1
    
# Variable to keep the main loop running
RUNNING, PAUSE = 0, 1
state = RUNNING

# Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))


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
    
# Update the display
pygame.display.flip()
    
    #time.sleep(.5)

    
