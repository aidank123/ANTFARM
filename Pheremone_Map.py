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

#updated while an ant is returning home with food so other ants know there is food there
home_pheremone_map = np.zeros((MAP_WIDTH, MAP_HEIGHT))
#updated while an ant is searching for food so it knows how to return
food_pheremone_map = np.zeros((MAP_WIDTH, MAP_HEIGHT))
        
class Pheremone_Map:
    
    def set_food_pheremone_map(self, new_map):
        food_pheremone_map = new_map
        
    def get_food_pheremone_map(self):
        return food_pheremone_map
    
    def set_home_pheremone_map(self, new_map):
        home_pheremone_map = new_map
        
    def get_home_pheremone_map(self):
        return home_pheremone_map
    
    def update_food_map(self, value, location):
        x = location[0]
        y = location[1]
        
        food_pheremone_map[x][y] += value
        self.set_food_pheremone_map(food_pheremone_map)
        
    def update_home_map(self, value, location):
        x = location[0]
        y = location[1]
        
        home_pheremone_map[x][y] += value
        self.set_home_pheremone_map(home_pheremone_map)
        
    def pheremone_decay(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                
                if(home_pheremone_map[x][y] >= .005):
                    home_pheremone_map[x][y] -= .005
                    self.set_home_pheremone_map(home_pheremone_map)
                
                if(food_pheremone_map[x][y] >= .005):
                    food_pheremone_map[x][y] -= .005
                    self.set_food_pheremone_map(food_pheremone_map)
        
        