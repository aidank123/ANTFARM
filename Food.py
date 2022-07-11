import pygame
import Globals as gl


#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()
food_locations = []

class Food:
    def __init__(self):
        self.map = map
        
    def add_location(self,location):
        food_locations.append(location)
        
    def get_map(self):
        return food_locations