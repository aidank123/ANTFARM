# Define a ant object by extending pygame.sprite.Sprite
# The surface drawn on the MAP is now an attribute of 'ant'
import pygame
import random
import Pheremone_Map as pm
import Globals as gl
import Pathing as p
import Functions
#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()
ANT_COLOR = g.get_ant_color()

pathing = p.Pathing()
f = Functions.Functions()
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

p = pm.Pheremone_Map()

class Ant(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Ant, self).__init__()
        self.surf = pygame.Surface((3, 3))
        self.surf.fill(ANT_COLOR)
        self.rect = self.surf.get_rect()
        self.has_food = False
        
        #initiating ants to hive location. Right now its better to stick with the one location
        for h in HIVE_LOCATIONS:
            x = h[0]
            y = h[1]
            self.rect.x = x
            self.rect.y = y
    
    #add location to pheremone map
    def add_location(self):
        p.add_location([self.rect.x, self.rect.y])
        
    # Keep player on the screen
    def stay_on_screen(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > MAP_WIDTH:
            self.rect.right = MAP_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= MAP_HEIGHT:
            self.rect.bottom = MAP_HEIGHT
    # Move the sprite based on user keypresses
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
        
        self.stay_on_screen()
            

    def random_pathing(self):
        rand = random.randint(0,3)
        if rand == 0:
            self.rect.move_ip(0, -1)
        if rand == 1:
            self.rect.move_ip(0, 1)
        if rand == 2:
            self.rect.move_ip(-1, 0)
        if rand == 3:
            self.rect.move_ip(1, 0)
        
    
        self.stay_on_screen()
        
    def ant_location(self):
        x = self.rect.x
        y = self.rect.y
        return [x,y]
    
    def Pathing(self):
             
        
        if (self.has_food == False):
            self.update_home_map()
            self.check_for_food()
            
        elif(self.has_food == True):
            self.update_food_map()
            self.drop_off_food()             
                    
        #calling this method will return the chosen move, the ant will then move to that location
        chosen_move = pathing.local_search(self.ant_location(), self.has_food)
        
        #setting x and y to be the coordinates of the chosen move
        self.rect.x = chosen_move[0]
        self.rect.y = chosen_move[1]

        
        self.stay_on_screen()
    
    #method that determines if an ant has encountered food in the 8 surrounding squares   
    def check_for_food(self):
        
        if(self.has_food == False):
            for p in f.adjacent_squares(self.ant_location()):

                if p in FOOD_LOCATIONS:
                    self.has_food = True
                    

    #method that determines if an ant has encountered the hive in the 8 surrounding squares
    def drop_off_food(self):
        
        if self.has_food == True:
            for p in f.adjacent_squares(self.ant_location()):

                if p in HIVE_LOCATIONS:
                    self.has_food = False

    
    def update_food_map(self):
        p.update_food_map(self.ant_location())
        
    def update_home_map(self):
        p.update_home_map(self.ant_location())