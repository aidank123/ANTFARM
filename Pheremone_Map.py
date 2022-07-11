import numpy as np
import Globals as gl


#IMPORT GLOBALS INTO EVERY CLASS

#creating globals object and calling each method
g = gl.Globals()
NUMBER_OF_ANTS = g.get_number_of_ants()
MAP_HEIGHT = g.get_height()
MAP_WIDTH = g.get_width()
HIVE_LOCATIONS = g.get_hive_locations()
FOOD_LOCATIONS = g.get_food_locations()

class Pheremone_Map:
    def __init__(self):
        #updated while an ant is returning home with food so other ants know there is food there
        self.home_pheremone_map = np.zeros((MAP_HEIGHT, MAP_WIDTH))
        #updated while an ant is searching for food so it knows how to return
        self.food_pheremone_map = np.zeros((MAP_HEIGHT, MAP_WIDTH))
        
    def get_food_pheremone_map(self):
        return self.food_pheremone_map
    
    def get_home_pheremone_map(self):
        return self.home_pheremone_map
    
    def update_food_map(self, value, location):
        x = location[0]
        y = location[1]
        
        self.food_pheremone_map[x][y] += value
        
    def update_home_map(self, value, location):
        x = location[0]
        y = location[1]
        
        self.home_pheremone_map[x][y] += value
        
        